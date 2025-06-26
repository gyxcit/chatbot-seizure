the movement detected exceeds the movement threshold, then R roi else if SD = False & AS = 3 then
is calculated as the ratio between (P roi ) and (Ps) which can be update AS =2
expressed as DoAnalysis(At)
R roi = P P r s oi (2) else end
A seizure is then detected if R roi ≥ the algorithms sensitivity AS ==AS
threshold.Ifthesensitivitythresholdisexceededforthreeconsecutive Alert ’Input not received’
timesteps,analarmstateisraised,andthedatasavedtothedatabase. DoAnalysis(At)
Three consecutive timesteps (15 seconds) were utilised to give bal-
end
ance between reducing false alarms and ensuring prompt generation
ofanalarmwhenagenuineseizurewasdetected.Theaboveprocess