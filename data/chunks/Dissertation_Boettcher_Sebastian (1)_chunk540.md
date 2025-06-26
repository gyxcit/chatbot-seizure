To assess the performance of seizure detection across multiple patients, the GBT model was
firsttrainedusingtheperi-ictalseizuredataofthe12seizuresfromthethreeparticipantsmen-
tionedabove. Themodelwastherebyparameter-optimizedinaLOPOmanner,asexplainedin
Section5.2.2. Inthiscross-validation,themodelwiththebest-performingparametercombina-
tionwasabletorecognizeatotalofeightofthetwelveseizures(overallsensitivity67%,mean
72%, and range 50% to 100%) in the validation set, with a mean FAR of approximately one116
CHAPTER5.
DETECTIONOFFOCALONSETSEIZURES
Table 5.6: Evaluation results for the intra-subject leave-one-seizure-out evaluation, and the inter-subject leave-one-participant-out eval-