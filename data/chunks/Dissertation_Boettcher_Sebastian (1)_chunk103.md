and evaluation need to be completely separate from the data the model was trained
with. Accordingly, the data set is split into training and test data sets before creating
the model, such that the trained model has never seen any of the data in the test set.
In seizure detection, this is optimally done by selecting the test data from a different
patient cohort than the training data, or at least selecting it from other patients in the
same cohort, in the case of generic model evaluation. For individualized models, the
test data would comprise the complete rest of the data for a particular participant, that
was not selected for the training process, whereby the training data would comprise a