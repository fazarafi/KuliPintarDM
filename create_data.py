from data_service.mongo_accessor import TweetDataMongoAccessorSingleton

data_training = []

db = TweetDataMongoAccessorSingleton.getInstance()
coll = db.coll

with open("twitter_data_training.txt") as f:
    for line in f:
        single_data = (line,'keluhan')
        data_training.append(single_data)
        print(data_training)

cursor = coll.find().limit(100)
for tweet in cursor:
    single_data = (tweet["message"],'non-keluhan')
    data_training.append(single_data)

i = 0
for test in data_training:
    i = i + 1
    print(test)
    print(i)
