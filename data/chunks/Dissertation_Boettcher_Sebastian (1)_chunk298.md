modality, serializes and schematizes that data, and stores it for the short-term. Thereby, it
can efficiently handle multiple clients sending data in parallel and in real-time while keeping
references to client identifier, biosignal modality, and other metadata, per sample. In a next
step,the receivedandprocesseddataare transferredtoamore long-termstoragecomponent
(Apache Hadoop distributed file system (HDFS)), saving the data on disk and easily accessible
tootherprocessesontheserver. Inordertofacilitatedataanalysisandsharing,inafinalstep
thedataareencodedintohuman-readablecomma-separatedvaluesfiles,whichcanbecopied
toothercomputersandeasilyreadintostandarddataanalysissoftware.