lengths of 2s, 10s and 20s for the ACC features and 5min, 10min and 20min for the EDA
features, a total of 453 features were calculated for each fixed time point. Note the large dif-
ference in window lengths for EDA vs. ACC; Since the EDA signal is primarily analyzed for
tonicactivityfeatures,andthetimeframeofchangeinEDAsignalsisintheorderofminutes,
the window lengths for EDA were chosen like this. Furthermore, for this evaluation the time
interval between feature points is fixed at T = 1s. To avoid feature intervals with undefined
values,featureextractionisonlydoneonsectionsofthedatawhereallmodalitiesarepresent,
thatis,wherethereisadatapointinallmodalitiesforagiventimestamp.