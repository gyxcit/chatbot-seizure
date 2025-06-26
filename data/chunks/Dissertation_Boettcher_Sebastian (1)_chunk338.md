manner. The model is improved with each new weak learner that is added to the ensemble,
whereastheRFmodeltrainsalltreesinparallelandindependentofeachother. Weaklearners
in this case are trees with a very low number of splits, down to decision stumps with just 1
split. ThisresultsinanoveralllowerbiasandsimilarvarianceforGBTmodelscomparedwith
RF models at the cost of higher parameter tuning effort. Therefore, GBT models generally
perform better than RF models if tuned sufficiently, and they have been successfully used in
machine learning problems [95]. To tackle this tuning effort, a hyperparameter optimization