to the next steps in long-sequence data. Another drawback of RNN is the vanishing
gradientproblem[30–33]. Theproblemarisesbecauseoftheshrinkingofgradientsasit
back-propagates. Tosolvetheshort-termmemoryproblem,LSTMgateswerecreated[30].
Theflowofinformationcanberegulatedthroughgates. ThegatescanpreservethelongInt.J.Environ.Res.PublicHealth2021,18,5780 14of33
sequenceofnecessarydata,andthrowawaytheundesiredones. Thebuildingblockof
LSTMisthecellstateanditsgates.
Figure10.SampleRNNmodelthatcanbeusedforseizuredetection.
In this section, Golmohammadi et al. [68] evaluated two LSTM architectures with
three and four layers together with the Softmax classifier in their investigation and ob-