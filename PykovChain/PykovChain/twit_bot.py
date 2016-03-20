#Python twit bot using a Markov chain text generator
#author: Morgan Osborn

import tweepy
import pykov
import setEnv
import os
import botConfig

#setEnv.setupEnv()

filename = os.environ['TEXT_ADDR']

#setup twitter auth stuff
auth = tweepy.OAuthHandler(os.environ['CONSUMER_K'], os.environ['CONSUMER_S'])
auth.set_access_token(os.environ['ACCESS_K'], os.environ['ACCESS_S'])
api = tweepy.API(auth)


def doTweet ():
    openersname = botConfig.openersName
    corpusname = botConfig.corpusName

    pykov.genCorpus(filename, corpusname, openersname)
    
    phrase = ("", True, 0)
    #gen until an appropriately sized result
    while phrase[2] > 139 or phrase[2] < botConfig.minLen and phrase[1] == True:     #length should be CONFIG
        phrase = pykov.genPhrase(corpusname, openersname)


    print(phrase[0])
    api.update_status(phrase[0])


doTweet()
