#Python twit bot using a Markov chain text generator
#author: Morgan Osborn

import tweepy
import pykov
import setEnv
import os

#setEnv.setupEnv()

filename = os.environ['TEXT_ADDR']

#setup twitter auth stuff
auth = tweepy.OAuthHandler(os.environ['CONSUMER_K'], os.environ['CONSUMER_S'])
auth.set_access_token(os.environ['ACCESS_K'], os.environ['ACCESS_S'])
api = tweepy.API(auth)


def doTweet ():
    openers = []
    corpus = pykov.genCorpus(filename, openers)

    phrase = ""
    #gen until an appropriately sized result
    length = 0
    while length > 139 or length < 20:
        phrase = pykov.genPhrase(corpus, openers)
        length = len(phrase)

    print(phrase)
    api.update_status(phrase)


doTweet()
