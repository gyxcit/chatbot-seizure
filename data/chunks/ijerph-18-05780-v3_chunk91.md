AppendixA
Table A1 shows the detailed summary of DL methods employed for automated
detectionofepilepticseizures.Int.J.Environ.Res.PublicHealth2021,18,5780 24of33
TableA1.SummaryofDLmethodsemployedforautomateddetectionofepilepticseizures.
Work Dataset Preprocessing DLToolbox DLNetwork K-Fold Classifier Accuracy(%)
Down-Sampling,
[50] Clinical Normalization,Data Keras SeizNet – – –
Augmentation
[51] CHB-MIT Visualization PyTorch 2D-CNN – Softmax 98.05
Filtering,Normalization,
[52] Clinical NA 2D-CNN 10 Softmax NA
Visualization
[53] TUH DivSpec PyTorch SeizureNet 5 Softmax NA
[54] Clinical STFT NA TGCN – Sigmoid NA
[55] CHB-MIT SpatialRepresentation NA 2D-CNN – Softmax 99.48