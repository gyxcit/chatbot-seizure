optimization runs. The boosting method used in the model was adaptive boosting for binary
classification [310], and the misclassification cost for false negatives was always 1. The hy-
perparameter optimization resulted in an optimal set of parameters that were subsequently
usedinallthetestingsteps. Theoptimalparametercombinationwaschosenasthecombina-
tion that achieved the highest sensitivity and lowest false alarm rate (FAR) during the LOPO
validation run of the parameter combination, prioritizing sensitivity. Model parameters not
specifiedherewereleftattheirdefaultvalues.
Evaluation
Toprocessthemodeloutputandscoreitsperformancewhencomparedwiththegroundtruth,