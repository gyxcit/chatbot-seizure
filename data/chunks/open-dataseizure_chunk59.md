5 BatchSize 24
A. PreprocessingandDataEngineering
By utilising the OSTK WebApi connector, data was extracted
as a JSON string and subsequently transformed by flattening the
hierarchical structure of the data’s nested objects and loaded as
a dataframe for manipulation. Data cleaning, analysis, and feature
engineering were conducted to prepare the data for classification.
To address the issue of imbalanced data, random oversampling was
applied to the minority class. In order to mitigate the effects of
data duplication resulting from oversampling, Gaussian noise was
introducedtotheACMdataasaformofdataaugmentation,thereby