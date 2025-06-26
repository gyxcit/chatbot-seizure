and validation set pairs. These are then used in a k-fold cross-validation, gauging the performance of a model with a specific parameter
combination. Thisstepisrepeatedwitheachpossibleparameterset,findingtheoptimalparameterstouseinthefinalmodel.18 CHAPTER1. INTRODUCTION
ModelCreationandOptimization: The process of creating a detection model with the
GBT algorithm includes a parameter optimization step before training the final model
withdata. Figure1.4billustratesamoredetailedoverviewoftheparameteroptimization
process as it was implemented in the seizure detection pipeline employed here. Param-
eteroptimizationiscarriedoutasfollows: