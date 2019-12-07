# AdaptingVQAtoPronounRes

Welcome to our repo! This is our attempt at the Winograd Schema Challenge. 

We ask that you read through our paper on our work; it describes most of what we are doing.

In this repo are our scripts for generating data to be embedded (*generator.py), the CSVs that we have fed into our embeddings, the datasets, and our models.

Feel free to run any of them to verify; we used Python3 for this project, so it is required. Simply clone our repo and run any of our scripts. All the data should be in the correct spot for referencing.



After data creation is done:

For Hypothesis-1:
You need to use the EmbeddingsForNLPProj notebook and to reproduce our results, go to the save and load data section and execute the imports and then the only other uncommeented cell after uploading the required files which can be seen in that cell.

Once that is done, proceed to the next section. You might need to run the classifier a few times before you achieve our reported results as the MLPClassifier is not stable and does not converge to the same minima every time.


For Hypothesis-2:
You need to go to PosTag notebook and run it. The results in Hypothesis-2 are exactly the same as Hypothesis-1 currently. Hence, running that might not be of much use.