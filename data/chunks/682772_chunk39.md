either as a single JSON script containing data for all labelled events "hasHrData": true,
"hasO2SatData": false,
or as a subset focusing on specific event types such as tonic-clonic
"hrThreshMax": 150,
or false alarms. The datasets are organised hierarchically using a
"hrThreshMin": 40,
one-to-many relationship, where each event has multiple sub-events. "hrAlarmActive": false,
Each sub-event corresponds to a 5-second timestep, and sensor data "phoneAppVersion": "4.1.2",
for that timestep is stored as a JSON array called ”Datapoints.” The "sampleFreq": 25,
"watchFwVersion": "2.4.9",
complete JSON schema of the OSDB, including accurate attribute
"watchPartNo": "006-B2337-00",