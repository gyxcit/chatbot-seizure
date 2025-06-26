window lengths at the same time for later analysis of the best combination of features and
windowlengths. Morespecifically,theresultingtablesoffeatureswillhavevaluesatthesame
timepointsforallmodalitiesandallwindowsizes,allowingthefeaturedatatobeconcatenated
into one table for model training. Figure 5.2 shows a graphical representation of this mixed
featureset.
Thefeaturesetforthisevaluationconsistsof141ACCfeaturesfromthetimeandfrequency
domains (divided into 40 subgroups when grouping together x, y, z, and total features), and
anadditional10EDAfeatures,someofwhicharealsocorrectedforabaseline. Withwindow
lengths of 2s, 10s and 20s for the ACC features and 5min, 10min and 20min for the EDA