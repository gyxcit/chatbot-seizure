new raw data, and decode them from a binary format to appropriate floating-point numbers.
The Empatica E4 sends data in batches, which the app receives together with a time stamp
per sample that derives from the wearable’s internal real-time clock. This clock is updated
to the current time of the Android companion device only at the start of each connection
session. Theappthencollectsallofthesesamplesofrawdata,groupedbybiosignalmodality,
supplementing each with a secondary time stamp of the Android operating system (OS) time
atthemomentofreceiving. ThisOS-specifictimeisregularlysynchronizedwiththeinternal
timeofthevideo-electroencephalography(vEEG)systemoftheepilepsymonitoringunit. The