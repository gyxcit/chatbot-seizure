ner on the training set. The data for 1 of the 8 participants in the training set were kept back
as a validation set, and the model was trained on the seizures from the other 7 participants,
usingonly10minperi-ictaldataforeachseizure. Thisreductionofthetrainingdatatoonlya
small period around seizures helps with the large imbalance in the data set when comparing
ictal and non-ictal epochs. Once the model was trained, it was then tested on the complete
dataofthevalidationparticipantintherespectiveround,andtheprocesswasrepeated7more
times,cyclingthroughtheparticipantsforvalidation. Themeanscoreofthe8validationruns
wasthensavedastheperformanceofthecurrentparametercombination,andtheentireval-