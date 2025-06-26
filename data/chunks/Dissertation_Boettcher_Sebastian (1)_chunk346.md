long to a seizure or not. Comparing the ground truth and the prediction labels for evaluation
can be done sample-wise by comparing each 2-second interval, or event-wise, by combining
consecutiveintervalsofthepositiveclasstodistinctevents. Inthisanalysisthelattermethod
waschosen,whichrequirespostprocessingofthemodeloutput.4.1. DETECTIONOFTONIC-CLONICSEIZURES 71
First,thepredictionoutputofthemodelwassmoothedwithahysteresis-likefiltertoavoid
single-sample positives or gaps in consecutive positive predictions. To this end, all gaps be-
tween consecutive positive predictions smaller than 20 seconds in duration were filled out as