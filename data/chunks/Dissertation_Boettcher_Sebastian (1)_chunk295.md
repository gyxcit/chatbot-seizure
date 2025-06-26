application that connects to the wearable by Bluetooth. Furthermore, a data ingest and pro-
cessinginfrastructurewasdeployedonaservermachine,handlingthedatacollectedandsent
by the app via standard wireless network connection. The raw data were then stored on a
network-attachedstorageserverinhuman-readable,comma-separatedtextfilesforlaterpro-
cessing and analysis. Figure 3.4 gives an overview of the full data collection pipeline, as also
furtherdescribedinthefollowing.
The Android app uses a SDK provided by the manufacturer to connect to the E4, receive
new raw data, and decode them from a binary format to appropriate floating-point numbers.