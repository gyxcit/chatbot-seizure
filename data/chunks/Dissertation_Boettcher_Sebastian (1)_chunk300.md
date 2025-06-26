ples,correctionoftimestampdrift,anddiscoveryofviabledatablocks.
The timestamps attached to each sample of wearable data, both the native E4 stamp and
the Android OS time, are given as Unix time1, that is, the number of seconds elapsed since
1970-01-01 00:00:00 UTC. Here,the timestamps arenumbers infloating-point for-
matatmillisecondprecision. TherawEmpaticaE4datacansometimescontaintwodatasam-
ples with the exact same timestamp, due to unknown device-internal reasons. Data analysis
methodologies generally expect time series data to be unique with respect to sample times-
tamps. Thus, immediately after reading the data into memory, samples with the same times-