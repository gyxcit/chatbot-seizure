EEGsignalsarefirsttransformedintotwo-dimensionalplotsbyemployingvisualization
methods such as spectrogram [43], higher-order bispectrum [44,45], and wavelet trans-
forms,andarethenappliedtotheinputoftheconvolutionalnetwork. In1Darchitectures,
the EEG signals are applied in the one-dimensional form to the input of convolutional
networks. Inthesenetworks,changesaremadetothecorearchitectureof2D-CNNthat
makes it capable of processing the 1D-EEG signals. Therefore, since both 2D and one-
dimensionalconvolutionalneuralnetworks(1D-CNNs)areusedinthefieldofepileptic
seizuresdetection,theyareinvestigatedseparately.
A.2DConvolutionalNeuralNetworks(2D-CNNs)