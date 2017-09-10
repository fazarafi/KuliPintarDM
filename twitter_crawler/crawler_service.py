import tweepy

class CrawlerService(object):

    consumer_key= 'kZ49PgRUF9mBDcXPP8p36JRK4'
    consumer_secret= 'L0mqr0JuTveT7cy4UJWo9UKJpJWLEsmUju71luhH160JOzIdZ0'
    access_token='73326998-elawNJwGoLYSCKMwmHNkI2Cn6ECSjBFnKWmTO9kkc'
    access_token_secret='rDThchhEl8pPCYYVPq8xEMGCajl7fybaF1JC5KxlxEn4L'

    def __init__(self, city):
        self.city = city;
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(auth)

    def crawl(self, key_word):
        public_tweets = self.api.search(key_word)
        return public_tweets
