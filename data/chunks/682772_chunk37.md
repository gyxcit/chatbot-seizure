beta trial, adjustments were made to accommodate the storage of "dataSourceName": "Garmin",
SpO2 and three-dimensional ACM data. By utilising an SQLite "alarmFreqMax": 8,
database on the Android platform and integrating additional fea- "alarmFreqMin": 3,
"datapoints": [{
tures and sensors, the OSD project achieved scalability and ensured
"alarmPhrase": "OK",
compatibility. Design choices were driven by the goal of optimising "alarmState": 0,
data storage, capturing relevant sensor data, and improving overall "dataTime": "2023-05-15T06:45:56Z",
performance. "hr": 87,
"o2Sat": 0,
"rawData": [x1, x2, x2, ... ,x125],
D. DatabaseSchema "rawData3D": [x1, y1, z1, ... ,z375],
"roiPower": 4,