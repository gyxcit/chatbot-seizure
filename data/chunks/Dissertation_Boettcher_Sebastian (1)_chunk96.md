prominentandwidelyusedarebrieflydescribedhere:
Bagging: Bootstrap aggregation, also called bagging, is a method of independently training
multipleindividualclassifierswithrandomlysampleddatafromthetrainingdatasetin
parallel. Duringtesting,newdataarethengiventoallofthesesub-learnersandamajor-
ity vote decides on the output classification of the whole ensemble. This methodology
may mitigate over-fitting that would occur if only a single instance of the individual
learner was used, and thus will typically outperform them. It does however not help
with under-fitting as a high bias in each individual model still results in a high output