# UpliftModelling_Iml_team4
These are data from one of the first successful trials of adjuvant chemotherapy for 
colon cancer. Levamisole is a low-toxicity compound previously used to treat worm 
infestations in animals; 5-FU is a moderately toxic (as these things go) chemotherapy 
agent. There are two records per person, one for recurrence and one for death.

Jest tutaj mowa o raku jelita grubego i eksperymentalnym podejściu do leczenia. 
Użyty był lek Levamisole - który jest stosowany u zwierząt jako lek przeciwrobaczy, ale 
zauważono jego właśniwości do leczenia raka jelita grubego. Do porównania jest drugi lek 
5-FU, czyli 5-Fluoro-Uracyl, który się stosuje "standardowo" w leczeniu raka jelita grubego
To jest ten "mocniejszy" lek. Oba te leki podaje się po opreacji wycięcia raka, jest to 
adjutowantowa chemia, czyli 'dodatkowa pooperacyjna'

Variable name                   | Done | Description
--------------------------------|------|--------------
id                              |  ✓   |    id
study                           |  ✓   | 	1 for all patients
rx                              |  ✓   |    Treatment - Obs(ervation), Lev(amisole), Lev(amisole)+5-FU
sex                             |  ✓   | 	1=male
age                             |  ✓   | 	in years
obstruct                        |  ✓   | 	obstruction of colon by tumour - jest to zwężenie okrężnicy przez tak, czyli zablokowanie przez guz
perfor                          |  ✓   |    perforation of colon - czy zrobiła się dziura w jelicie
adhere                          |  ✓   | 	adherence to nearby organs - przyleganie do okolicznych narzadów(np pęcherza moczowego)
nodes                           |  ✓   |    number of lymph nodes with detectable cancer - podczas operacji wycina się węzły chłonne które były zaatakowane przez raka i to jest liczba węzłów chłonych z wykrywalnym rakiem, powinno być dużo minimum 12, żeby operacja była 'udana'
time                            |      |    days until event or censoring - liczba dni do rozpoczęcia leczenia?
status                          |  ✓   |    censoring status
differ                          |  ✓   | 	differentiation of tumour (1=well, 2=moderate, 3=poor) - zróżnicowanie komórek guza - im więcej tym lepiej, bo bardziej przypomina komórki jelita, a nie zlepek nie wiadomo czego
extent                          |  ✓   |    Extent of local spread (1=submucosa, 2=muscle, 3=serosa, 4=contiguous structures) - Zasięg nowotworu, tzn do jakich tkanek dotarł, 1=podśluzowa, 2=mięśniowa, 3=surowicza, 4=przyległe struktury (im mniej tym lepiej)
surg                            |  ✓   | 	time from surgery to registration (0=short, 1=long) - czas od operacji do rejestracji
node4                           |  ✓   | 	more than 4 positive lymph nodes - 4 lub więcej węzłów chłonnych
etype                           |  ✓   | 	event type: 1=recurrence,2=death - nawrót lub śmierć
