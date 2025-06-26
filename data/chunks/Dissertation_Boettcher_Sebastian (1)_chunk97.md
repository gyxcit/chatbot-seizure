with under-fitting as a high bias in each individual model still results in a high output
bias. The method of aggregating specifically decision tree models in this way is called
randomforest [93,94].
GradientBoosting: Contrarytobagging,gradientboostingtrainsmultiplespecificallyweak
learnersthatareonlyslightlybetterthanchance,anddoessoiterativelyandnotinpar-
allel. Theoutputofthewholeensembleisdescribedasaweightedsumoftheindividual
learners’ outputs. For each new learner that gets added to the ensemble the training
samples are also weighted proportional to their error in the previous iteration by some
loss function, such that new learners target training samples with worse performance.