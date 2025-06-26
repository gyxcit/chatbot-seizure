thesedataformasignificantpartoftheinformationintheworld, compellingtheneed
forDL-basedschemestoprocessthesetypesofdata. RNNsarethesolutionsuggested
to overcome the mentioned challenges, and are widely used for physiological signals.
Figure 10 shows a general form of RNN used for epileptic seizure detection. In the
followingsection,anoverviewofpopularRNNmodelsarepresentedinadditiontothe
reviewedpapers.
A.LongShort-TermMemory(LSTM)
The main problem of a simple RNN is short-term memory. RNN may leave out
key information as it has a hard time transporting information from earlier time steps
to the next steps in long-sequence data. Another drawback of RNN is the vanishing