The main indicators of performance used in this evaluation are the mean sensitivity, false
alarmrate(FAR)per24h(falsealarmrateper24h(FAR24))andpositivepredictivevalue(PPV).
Thesescoreswerecalculatedfromthenumberofoverlapsofseizureeventsinthegroundtruth
andpredictedlabels. Thelabeldata,analogoustothefeaturedata,werestoredat2sintervals,
and seizure events here were defined as consecutive intervals of labels classified as a seizure
of at least 6s and at most 10min. The output of the classification model was furthermore
smoothed before this scoring computation, by filling out gaps between seizure labels of at
most30s,andremovinganyorphanseizurelabels. Afterthisprocessingofthemodeloutput,