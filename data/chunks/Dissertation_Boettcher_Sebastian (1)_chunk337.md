overasegmentofdata. Thisenablestheuseofthecomplete,mergedfeaturespaceasthesin-
gleinputintoadetectionmodelfortraining[106]. Theintervalbetweenthefixedtimepoints
for feature calculation was chosen to be 2 seconds. Figure 5.2 and Figure 5.5 give a graphical
representationofthefeaturecomputationmethodology.
SeizureDetection
A gradient boosted decision trees (GBT) model [309] was used as the detection model for the
TCSs. Although similar to the well-known random forest (RF) method in being a set of trees
that are grown with training data, a GBT model builds trees as weak learners in an additive
manner. The model is improved with each new weak learner that is added to the ensemble,