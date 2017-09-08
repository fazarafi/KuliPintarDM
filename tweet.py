class Tweet(object):
	def __init__(self, text=None, tweet_class='non-keluhan'):
		self.text = text
		self.tweet_class = tweet_class

	def get_text(self):
		return self.text

	def get_tweet_class(self):
		return self.tweet_class

	def set_text(self, text):
		self.text = text

	def set_tweet_class(self, tweet_class):
		self.tweet_class = tweet_class
