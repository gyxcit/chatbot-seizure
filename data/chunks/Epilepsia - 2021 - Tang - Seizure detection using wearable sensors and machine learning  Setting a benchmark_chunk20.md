and EEG clock as the time difference between the wristband CNN models are shown in Figure 2.
and EEG clock at the beginning of the experiment (Figure Our CNN model consists of two convolutional layers.
S1b). Figure 1A shows the distribution of start timing errors Convolutional Layer 1 is followed by Rectified Linear Unit
observed in our study; absolute errors follow approximately (ReLU) and dropout operations. Convolutional Layer 2 is fol-
a Gaussian distribution and are predominantly shorter than lowed by ReLU and max pooling. The final layer is a global
20 s. average pooling29 layer. The network outputs are probabilis-