import random
from nltk.corpus import names
import nltk

nltk.download('names')

def gender_features(word):
    return {'name': word}

labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                 [(name, 'female') for name in names.words('female.txt')])
random.shuffle(labeled_names)

featuresets = [(gender_features(n), gender)
               for (n, gender) in labeled_names]

# Divide the resulting list of feature
# sets into a training set and a test set.
train_set, test_set = featuresets, featuresets

# The training set is used to
# train a new "naive Bayes" classifier.
classifier = nltk.NaiveBayesClassifier.train(train_set)

for pair in labeled_names:
    print(classifier.classify(gender_features(pair[0])))

# output should be 'male'
print(nltk.classify.accuracy(classifier, train_set))

# it shows accurancy of our classifier and
# train_set. which must be more than 99 %
#classifier.show_most_informative_features(100)