from apscheduler.schedulers.blocking import BlockingScheduler
from twitter_crawler.crawler_service import CrawlerService
from data_service.mongo_accessor import TweetDataMongoAccessorSingleton
from bson.objectid import ObjectId
import logging

sched = BlockingScheduler()

# @sched.scheduled_job('interval', seconds=10)
# def timed_job():
#     print('This job is run every three minutes.')
#     tweet_data = TweetDataMongoAccessorSingleton.getInstance()
#     tweet_data_collection = tweet_data.coll
#     cursor = tweet_data_collection.find({'_id':ObjectId("59b4f8b5337c7a15fc0c3786")})
#     for document in cursor:
#         print(document)

@sched.scheduled_job('interval', seconds=50)
def crawler_jakarta():
    crawler_operator('jakarta')

@sched.scheduled_job('interval', seconds=50)
def crawler_bandung():
    crawler_operator('bandung')

@sched.scheduled_job('interval', seconds=50)
def crawler_medan():
    crawler_operator('medan')

@sched.scheduled_job('interval', seconds=50)
def crawler_makassar():
    crawler_operator('makassar')

@sched.scheduled_job('interval', seconds=50)
def crawler_surabaya():
    crawler_operator('surabaya')



def crawler_operator(city):
    print("")
    print("")
    print("Crawling "+city)
    print("")
    print("")
    tweet_data = TweetDataMongoAccessorSingleton.getInstance()
    tweet_data_collection = tweet_data.coll
    city_key = city
    crawler = CrawlerService(city_key)
    message = crawler.crawl(city_key)
    for tweet in message:
        if (tweet_data_collection.find({'message':tweet.text}).count() == 0):
            print(tweet.text)
            data = {}
            data["city"] = city_key
            data['message'] = tweet.text
            tweet_data_collection.insert(data)

log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)
sched.start()
