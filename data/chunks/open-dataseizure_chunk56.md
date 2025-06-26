spatialdimensionality.Theoutputvectorfromb 4 isflattenedandfed
intothemodelsclassificationblockwhichhasthreedenselayers.The
IV. THE OPEN SEIZURE TOOLKIT firsttwodenselayerscontain128fullyconnectedneuronswithReLU
The Open Seizure Toolkit is a software package developed by activationunits,whilethethirdlayerincorporatesasoftmaxactivation
OSD, serving to facilitate data access to the OSDB, enabling the function to produce an output vector of multiple probabilities. Cate-
analysis and development of seizure detection models compatible gorical cross-entropy loss was used to optimise the learning process