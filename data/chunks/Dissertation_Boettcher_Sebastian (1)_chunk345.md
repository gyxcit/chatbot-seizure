Evaluation
Toprocessthemodeloutputandscoreitsperformancewhencomparedwiththegroundtruth,
the same method was used both in the validation during hyperparameter optimization and
later during the testing phase (see Section 4.1.3). Owing to the method of feature extraction
at fixed time intervals of 2 seconds, the output of the GBT model is a prediction vector con-
tainingthepredictedlabelevery2seconds. Theinputlabels,thatis,thegroundtruth,andthe
predictedlabelswerebinary,denotingtheclassificationofeach2-secondintervaltoeitherbe-
long to a seizure or not. Comparing the ground truth and the prediction labels for evaluation