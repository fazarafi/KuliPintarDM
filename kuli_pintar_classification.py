from textblob.classifiers import NaiveBayesClassifier
from sklearn.naive_bayes import GaussianNB
from tweet import Tweet
from data_service.mongo_accessor import TweetDataMongoAccessorSingleton
import time

class TweetClassifier(object):
	def __init__(self, classifier=None):
		self.classifier = classifier

	def get_classes():
		return ["keluhan","non-keluhan"]

	def preprocessing(self, object):
		return object

	def train_data(self, train):
		start = time.time()
		cl = NaiveBayesClassifier(train)
		clf = GaussianNB()

		end = time.time()
		self.classifier = cl
		return end-start

	def test_data(self, test):
		keluhan_tweets = []
		for tweet in test:
			tweet_class = self.classifier.classify(tweet)
			if (tweet_class == 'keluhan'):
				keluhan_tweets.append(tweet)
		return keluhan_tweets



#START MAIN
train = []

data_accessor = TweetDataMongoAccessorSingleton.getInstance()
coll = data_accessor.coll

with open("twitter_data_training.txt") as f:
    for line in f:
        single_data = (line,'keluhan')
        train.append(single_data)

cursor = coll.find().limit(100)
for tweet in cursor:
    single_data = (tweet["message"],'non-keluhan')
    train.append(single_data)

test = []
all_cursor = coll.find().limit(100)
for tweet in all_cursor:
	test.append(tweet["message"])

tweet_classifier = TweetClassifier()
print('Processing Time:',tweet_classifier.train_data(train),'seconds')
print('++++++++++++++++++++++++++++')
print("Tweet Keluhan Terdiri dari :")
keluhan_tweets = tweet_classifier.test_data(test)
for keluhan in keluhan_tweets:
 	print(keluhan)
