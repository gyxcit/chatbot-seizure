Fourdifferentmodelparameterswereoptimized: thelearningrate,themaximumnumber
ofweaklearners,themaximumtreedepthperweaklearner,andthemisclassificationcostfor
false positives (FPs). Conversely, the misclassification cost for false negatives (FNs) was not
tunedandkeptunweighted,andonlyonetypeofboostingwasused,namelyadaptiveboosting110 CHAPTER5. DETECTIONOFFOCALONSETSEIZURES
for binary classification (“AdaBoost”) [310]. In total, the number of different parameter com-
binations over which the grid search optimization was performed added up to 600. The best
parametercombinationwaschosenastheonewiththehighestsensitivityandlowestnumber