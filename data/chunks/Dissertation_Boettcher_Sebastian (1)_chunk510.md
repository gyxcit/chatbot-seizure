six seizures recorded for a single participant, or with multiple independent recordings of a
participant, this was performed without a dedicated test set which is truly “out-of-sample”.
Rather, the model was trained with the data of all but one seizure and the respective peri-
ictal data of 10min before and after each seizure. These data were standardized using the
z-score method before training, and the normalization parameters (centering mean and scal-
ing standard deviation) were stored. The resulting model was then tested on the remaining
participantdata,standardizedusingthepreviouslystorednormalizationparametersfromthe