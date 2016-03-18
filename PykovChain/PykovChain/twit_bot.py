#Python twit bot using a Markov chain text generator
#author: Morgan Osborn

import twit_keys
import tweepy
import pykov
import schedule
import time

filename = "bolano.txt"      #ñ

#setup twitter auth stuff
auth = tweepy.OAuthHandler(twit_keys.CONSUMER_KEY, twit_keys.CONSUMER_SECRET)
auth.set_access_token(twit_keys.ACCESS_TOKEN, twit_keys.ACCESS_SECRET)
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


schedule.every(8).hours.do(doTweet)

doTweet()           #tweet on boot, why not?
while True:
    schedule.run_pending()
    time.sleep(1)