import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

def read_prep_split(data_path):
    data = pd.read_csv(data_path, index_col = 0).drop(['id','study','etype'], axis = 1)
    data['treatment'] = np.where(data['rx']=='Obs', 0, np.where(data['rx']=='Lev',1,2))
    data.drop('rx', axis=1, inplace = True)
    data = data.fillna(-1)
    
    # numpy matrices version
#     X = df.drop('target',axis=1).to_numpy()
#     y = df.target.to_numpy()

    # pandas dataframes version
    X = data.drop('time',axis=1).reset_index(drop=True)
    y = data.time.reset_index(drop=True)
    
    return train_test_split(X, y, random_state = 123)


if __name__ == "__main__":
    X_train, X_test, y_train, y_test = read_prep_split('./survival.csv')
    
    X_train.to_csv("survival-data-split/survival_X_train.csv", index=False)
    X_test.to_csv("survival-data-split/survival_X_test.csv", index=False)
    y_train.to_csv("survival-data-split/survival_y_train.csv", index=False)
    y_test.to_csv("survival-data-split/survival_y_test.csv", index=False)