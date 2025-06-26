introducedtotheACMdataasaformofdataaugmentation,thereby
enhancing the variability among samples. Fig.9: A visual representation of accuracy and validation accuracy
plotted by the Open Seizure Toolkit”
B. ClassRelabellingandOneHotEncoding
In this experiment, one-hot encoding was used to convert 24
classcategoricalclasslabelsintoabinaryvectorrepresentation.The
resulting binary vectors contain all zero values except for the index
corresponding to the class label, which is set to 1. The nnTrainer.py
and processing pipeline.py scripts were then used to partition the
subset into a 75:25 split for the training and test sets, respectively.
C. NeuralNetworkTrainer