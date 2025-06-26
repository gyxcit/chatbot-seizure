smaller than this value may not be distinguishable [41]. update AS =0
To detect a ’seizure-like’ movement, the algorithm calculates the DoAnalysis(At)
average power for the whole spectrum (Ps) and then the average
else if SD = False & AS = 2 then
powerofthe3-8HzRegionofInterest(P
roi
)foreachtimestep.To
update AS =1
reduce the FAR, (Ps) is checked against a threshold to ensure that
Alert ’Seizure Detected’
thereisasufficientlevelofmovement,thusavoidingspuriousalarms
caused by measurement noise when there is minimal movement. If
DoAnalysis(At)
the movement detected exceeds the movement threshold, then R roi else if SD = False & AS = 3 then