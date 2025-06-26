ClassificationandPerformanceEvaluation: Thetestdataareprocessedbythemodelre-
sultinginaseriesofbinaryclassificationsforeachofthefeaturevectorsinthetestset,
either detecting an event or not. To evaluate these results, they are compared to the
correspondinggroundtruthlabels,andcertainscoringmetricsarecalculatedindicating
the performance of the model on this out-of-sample test data. In seizure detection this
is typically done by deriving ground truth and detection events from the sample-wise
labels and checking for overlaps between those events, such that an overlap between
a ground truth and prediction event would constitute a true positive, a predicted event