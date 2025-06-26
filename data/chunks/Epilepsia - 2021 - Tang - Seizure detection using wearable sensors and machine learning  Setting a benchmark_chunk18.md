ent clocks. To compensate for the time drift between the de-
vice and EEG clocks, we synchronized the device clocks at
the start of the device recording. After we turned on the re- 2.5 | Data analysis
cording device, we simultaneously pressed the device button
and EEG event marker button. This created a time tag on both 2.5.1 | ML techniques
the device and EEG recordings. When we placed two weara-
ble devices on the patient, the button press was done simulta- We used a convolutional neural network (CNN) to classify
neously for both. We recorded a video of the syncing process raw time series data and applied random undersampling to