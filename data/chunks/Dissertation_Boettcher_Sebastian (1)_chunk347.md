tween consecutive positive predictions smaller than 20 seconds in duration were filled out as
positive,thuscreatingcontinuous,longereventsfromshortneighboringpositivepredictions.
Thereafter, all consecutive positive predictions of a certain length were discarded. This value
was chosen to be 4 seconds, as it provides a good balance between discarding short, single-
sample predictions and still keeping possible relevant events. Thus, the prediction output of
the model can be matched to the ground truth per participant by counting overlaps of pre-
dictedpositiveeventswithapositivegroundtrutheventastruepositives(TPs)andpredicted