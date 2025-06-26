inputsignalsaresplitintotimewindowsandspectrogramareobtainedfromthem. Then,
theseplotsarefedtoafour-layerGRUnetworkwithaSoftmaxFClayerintheclassification
stage;98%accuracywasachieved. Inanotherstudy,Royetal.[104]employedafive-layer
GRUnetworkwithSoftmaxclassifierandachievedremarkableresults. Table4provides
thesummaryofrelatedworksdoneusingRNNs. Figure11showsthesketchofaccuracy
(%)obtainedbyvariousauthorsusingRNNmodelsforseizuredetection.Int.J.Environ.Res.PublicHealth2021,18,5780 15of33
Table4.SummaryofrelatedworksdoneusingRNNs.
Works Networks NumberofLayers Classifier Accuracy(%)
3
[68] LSTM Sigmoid NA
4
LSTM 96.67
[92] 3 Sigmoid
GRU 96.82
IndRNN 48 87.00
[93] NA
LSTM 4 84.35
LSTM