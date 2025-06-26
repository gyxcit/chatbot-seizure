differentdataanalysissteps,whichcanbeintegratedintoacompleteseizuredetectionpipeline
from raw input data to classification labels [84, 97, 98]. Figure 1.4a gives an overview of how
this pipeline was designed and implemented in the work presented here. Raw data are first
prepared through various different preprocessing steps before features are extracted in the
nextstep. Thefeaturevectorsarethenusedtooptimizeandtrainthemodel,andother,previ-
ously unseen test data are then processed by the same pipeline to be classified by the created
model. Lastly,themodelperformanceisevaluatedbycomparingtheclassificationstothetrue
labels. Thefollowingdescribesthesequenceofanalysisstepsinmoredetail: