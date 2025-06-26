most30s,andremovinganyorphanseizurelabels. Afterthisprocessingofthemodeloutput,
it was compared to the ground truth and any overlaps of seizure events were counted as true
positives. Seizure events in the ground truth but not in the detector output were counted as
FNs, and vice versa, seizure events in the output that were not present in the ground truth
were counted as FPs. Note that the comparisons described above are given a 2min margin
beforeandafterseizureeventsinthegroundtruth,whereinoverlapswithdetectedeventsstill
countastruepositives. Thiswasperformedtoaccountforsomeoftheuncertaintyrelatedto