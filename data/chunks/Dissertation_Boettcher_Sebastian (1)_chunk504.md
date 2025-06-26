thewindow.
Finally, the BVP raw data (derived device-internally from the PPG sensor) are processed
toaheartrate(HR)estimationfollowingtheproceduredescribedinGlasstetteretal.[348]: A
peaktrackingalgorithmwasappliedtofindlocalminimaintherawtimeseries[349],andthe
resulting inter-beat-intervals were processed to the HR estimation employing several filters
toproduceasmoothandmeaningfuloutput. ThisHRestimationaswellasaspectralentropy
scorerepresentingBVPsignalquality[159,348]wasusedasfeaturevalues. AstheBVPsignal
is highly sensitive to motion artifacts [173], using a signal quality index like this as a feature
forclassificationfollowstheprincipleofregardingartifactsasadditionalinformation,instead