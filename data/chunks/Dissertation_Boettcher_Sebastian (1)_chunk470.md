Thecross-validationforeachpatientwasrepeated20timestogiveaconfidentideaoftheRF
model performance. Additionally, a second round of tests was done, where the interval for
the feature data now is [s −55min;s ]+[s +5min;s +55min], thus excluding
start end end end
data from detection for 5min after a seizure was already recognized. This can be seen as the
simulationofapost-detectionpauseofdataanalysis,whichpreventsfalsepositivedetections
resultingfromlargeuncertaintyindatafollowingimmediatelyafteraseizure.
Before the scoring of the tests, the predicted labels are smoothed by a hysteresis function
withathresholdof10s. Effectively,thismeansallconsecutivepositivepredictionsoflessthan