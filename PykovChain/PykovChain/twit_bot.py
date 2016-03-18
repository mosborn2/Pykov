#Python twit bot using a Markov chain text generator I wrote
#author: Morgan Osborn

import twit_keys
import tweepy
import pykov

filename = "testtxt.txt"

#setup twitter auth stuff
auth = tweepy.OAuthHandler(twit_keys.CONSUMER_KEY, twit_keys.CONSUMER_SECRET)
auth.set_access_token(twit_keys.ACCESS_TOKEN, twit_keys.ACCESS_SECRET)
api = tweepy.API(auth)


openers = []
corpus = pykov.genCorpus(filename, openers)

phrase = ""

#gen a few for DEBUG
#for x in range(0,15):
#    phrase = pykov.genPhrase(corpus, openers)
#    print(phrase + "\n")

length = 0
while length > 139 or length < 20:
    phrase = pykov.genPhrase(corpus, openers)
    length = len(phrase)

api.update_status(phrase)