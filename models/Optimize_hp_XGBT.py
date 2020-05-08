import hyperopt as hp
from hyperopt import Trials,fmin,STATUS_OK, space_eval
import pickle
import pandas as pd
import numpy as np

from causalml.inference.meta import XGBTRegressor

import glob
import os 

def prepare_data_to_model(path='../data/survival.csv'):
    data = pd.read_csv(path, index_col = 0).drop(['id','study','etype'], axis = 1)
    data['treatment'] = np.where(data['rx']=='Obs', 0, np.where(data['rx']=='Lev',1,2))
    data.drop('rx', axis=1, inplace = True)
    data = data.fillna(-1)
    return data.drop(['treatment','time'], axis=1), data['treatment'], data['time']


def get_model(PARAMS):
    """
    Get model according to parameters
    """
    model = XGBTRegressor(  
        max_depth=PARAMS.get('max_depth'),
        min_child_weight=PARAMS.get('min_child_weight'),
        gamma=PARAMS.get('gamma'),
        colsample_bytree=PARAMS.get('colsample_bytree'),
        learning_rate=PARAMS.get('learning_rate'),
        n_estimators=int(PARAMS.get('n_estimators')),
        random_state=123
    )
    return model


### Step 1 : defining the objective function
def objective(params, n_folds=3):

    model = get_model(params)
    te, lb, ub = model.estimate_ate(X, treatment, y)
    score = -np.min(lb)
    return score

### step 2 : defining the search space
search_space = {
    'max_depth':hp.hp.choice('max_depth', np.arange(1,7,dtype=int)),
    'n_estimators':hp.hp.choice('n_estimators', np.arange(100,1000,50,dtype=int)),
    'learning_rate':hp.hp.uniform('learning_rate', 0.001, 1),
    'min_child_weight': hp.hp.uniform('min_child_weight', 0,1),
    'colsample_bytree': hp.hp.uniform('colsample_bytree', 0,1),
    'gamma': hp.hp.uniform('gamma', 0,1)
        }


MAX_EVALS = 500
bayes_trials = Trials()
X, treatment, y = prepare_data_to_model()

# Optimize
print("Optymalizacja zadania")
best = fmin(fn = objective, space = search_space, algo = hp.tpe.suggest, 
max_evals = MAX_EVALS, trials = bayes_trials)
best_params = space_eval(search_space,best)
print(best_params)
mod = get_model(best_params)
mod.fit(X, treatment, y)
te, lb, ub = mod.estimate_ate(X, treatment, y)
print('Average Treatment1 Effect (XGBoost): {:.2f} ({:.2f}, {:.2f})'.format(te[0], lb[0], ub[0]))
print('Average Treatment2 Effect (XGBoost): {:.2f} ({:.2f}, {:.2f})'.format(te[1], lb[1], ub[1]))
print()
    # save experiments
pickle.dump(best_params, open("pickles/best_params_no_status.pickle", "wb"))    
pickle.dump(mod, open("pickles/opt_XGBTRegressor_no_status.pickle", "wb"))
