F. OpenSeizureDetectorAlgorithm
For seizure detection during the beta trial, participants were in-
Algorithm 1 Pseudo code for the OSD algorithm where At =
structed to use the OSD Android application which runs a deter-
acceleration (vector magnitude) at timestep t, Ps = spectrum power,
ministic detection algorithm. Sensor data was transmitted from the
P
roi
=RegionofInterestpower,R
roi
=ROIRatio,Th=threshold.
participants’ Garmin device to the OSD application in five second
DoAnalysistakesAt asaninputparameteronarepeatingloopevery
timesteps at a sample frequency of 25Hz, resulting in 125 measure-
5 seconds. The acceleration values are passed to a FFT to convert