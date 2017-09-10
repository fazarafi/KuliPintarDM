from __future__ import print_function
from sklearn.feature_extraction.text import *
from sklearn.cluster import KMeans, MiniBatchKMeans
from sklearn.metrics.pairwise import pairwise_distances_argmin
from sklearn.datasets.samples_generator import make_blobs

import matplotlib.pyplot as plt
import collections
import time

class TweetClustering(object):
	def __init__(self, tweet_list=None, cluster_num=0, model=None, x_train_tfidf=None, total_tweets=0, processing_time=0, top_three_words=None):
		self.tweet_list = tweet_list
		self.cluster_num = cluster_num
		self.model = model
		self.x_train_tfidf = x_train_tfidf
		self.total_tweets = total_tweets
		self.processing_time = processing_time
		self.top_three_words = top_three_words

	def get_tweet_list(self):
		return self.tweet_list

	def set_tweet_list(self, tweet_list):
		self.tweet_list = tweet_list

	def get_cluster_num(self):
		return self.cluster_num

	def set_cluster_num(self, cluster_num):
		self.cluster_num = cluster_num

	def get_model(self):
		return self.model

	def set_model(self, model):
		self.model = model

	def get_model(self):
		return self.model

	def set_model(self, model):
		self.model = model

	def get_total_tweets(self):
		return self.total_tweets

	def get_processing_time(self):
		return self.processing_time

	def get_top_three_words(self):
		return self.top_three_words

	def cluster_data(self):
		tfidf_vectorizer = TfidfVectorizer(min_df=1)
		X = tfidf_vectorizer.fit_transform(dataset)
		self.total_tweets = len(dataset)
		model = MiniBatchKMeans(init='k-means++', n_clusters=self.cluster_num, batch_size=45,
		                      n_init=10, max_no_improvement=10, verbose=0)
		start = time.time()
		model.fit(X)
		self.processing_time = time.time()-start
		self.set_model(model)

		clusters = collections.deque(maxlen=self.cluster_num)
		for idx in range(self.cluster_num):
			clusters.append([])

		ttw = collections.deque(maxlen=self.cluster_num)
		for idx in range(self.cluster_num):
			ttw.append([])

		order_centroids = model.cluster_centers_.argsort()[:, ::-1]
		terms = tfidf_vectorizer.get_feature_names()
		for i in range(self.cluster_num):
			for ind in order_centroids[i, :3]:
				ttw[i].append(terms[ind])
		
		self.top_three_words = ttw    

		for tweet in dataset:
			Y = tfidf_vectorizer.transform([tweet])
			prediction = model.predict(Y)
			tweet_cluster_array = clusters[prediction[0]]
			clusters[prediction[0]].append(tweet)
		return clusters

	def draw_graph(self, object):
		return object

dataset = [
	'Bandung tidak enak, sering macet',
	'Saya tidak suka dengan walikota Bandung',
	'walikota Bandung sombong',
	'Kemarin, saya terkena banjir di Bandung',
	'Walikota Bandung tidak profesional',
	'Harga barang di Bandung sangat mahal',
	'Aku suka indomie goreng rasa rendang.',
	'Jakarta terkena musibah banjir bandang.',
	'Indonesia juara dunia dalam cabang olahraga Tenis.',
	'Jika kamu mampu untuk mengubah dunia, maka harus banyak persiapan.',
	'Halo! siapa nama anda.',
	'Kucing suka makan tikus.',
	'Kebunku dipenuhi tanaman kacang.',
	'Bandung memiliki suhu yang dingin.'
]

tweet_clustering = TweetClustering(dataset,5)

clusters = tweet_clustering.cluster_data()
for cluster_id in range(tweet_clustering.cluster_num):
	print('[',cluster_id,']')
	print("Cluster Percentage:",round(len(clusters[cluster_id])/tweet_clustering.get_total_tweets()*100,2),"%")
	print("Top terms per cluster:")
	for word in tweet_clustering.get_top_three_words()[cluster_id]:
		print('>',word)
	print()
	# print(clusters[cluster])

