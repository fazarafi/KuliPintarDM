from pymongo import MongoClient

class TweetDataMongoAccessorSingleton(object):
    _instance = None

    @staticmethod
    def getInstance():
        if TweetDataMongoAccessorSingleton._instance == None:
            TweetDataMongoAccessorSingleton()
        return TweetDataMongoAccessorSingleton._instance

    def __init__(self):
        if TweetDataMongoAccessorSingleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            TweetDataMongoAccessorSingleton._instance = self
            #Connecting to Mongo in localhost
            client = MongoClient()
            self.db = client.gemastik
            self.coll = self.db.tweet
