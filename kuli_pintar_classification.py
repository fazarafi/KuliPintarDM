from textblob.classifiers import NaiveBayesClassifier
from sklearn.naive_bayes import GaussianNB
from tweet import Tweet
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


train = [
	('Bandung tidak enak, sering macet','keluhan'),
	('Saya tidak suka dengan walikota Bandung','keluhan'),
	('Bandung memiliki udara yang sejuk','non-keluhan'),
	('Kemarin, saya terkena banjir di Bandung','keluhan'),
	('Walikota Bandung sangat ramah','non-keluhan'),
	('Walikota Bandung tidak profesional','keluhan'),
	('Harga barang di Bandung sangat mahal','keluhan'),
]
test = ['barang ramah','Walikota tidak baik','Jakarta sejuk']

text = ('aduhhhhhhhhh','keluhan')
train.append(text)
for t in train:
	print (t)

# tweet_classifier = TweetClassifier()
# print('Processing Time:',tweet_classifier.train_data(train),'seconds')
# print('++++++++++++++++++++++++++++')
# print("Tweet Keluhan Terdiri dari :")
# keluhan_tweets = tweet_classifier.test_data(test)
# for keluhan in keluhan_tweets:
# 	print(keluhan)
