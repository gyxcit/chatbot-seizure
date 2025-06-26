optimization only used the training set to keep the test set unknown to the model before
testing. All feature data were normalized between −1 and 1 before training and testing. For
training, the combined feature input for the model, that is, the peri-ictal feature data of 10
TCSs, were normalized, and for testing the complete feature data from the recordings for a
participant were normalized independent of the feature data of the other participants in the
testset.
ThehyperparameteroptimizationwasperformedinaLOPOnestedcross-validationman-
ner on the training set. The data for 1 of the 8 participants in the training set were kept back