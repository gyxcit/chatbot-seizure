Thefrequencyresolutionofthespectrumisthendeterminedbydi-
end
vidingthesamplefrequency(25Hz)bythenumberofmeasurements
for each 5-second timestep where SD = False do
(125) per timestep, resulting in a resolution of 0.2Hz. This resolu-
if SD = False & AS = 0 then
tion allows for effective detection and differentiation of frequency
AS ==AS
components with a precision of 0.2Hz. These calculations indicate
DoAnalysis(At)
thatthealgorithmcanaccuratelyidentifyfrequencycomponentsthat
are spaced at intervals of 0.2Hz, however any frequency differences else if SD = False & AS = 1 then
smaller than this value may not be distinguishable [41]. update AS =0