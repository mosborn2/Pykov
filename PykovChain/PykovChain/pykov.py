#Python Markov Chain generator for 2-word order chains
#author: Morgan Osborn

#currently build map per use, NOTGOOD

#TODO, fill pairs last array, make sure no empty strings anywhere, format into actual sentence

import random
import urllib.request
import pickle
import os.path


#generates corpus and TODO generates opening phrases by ref
def genCorpus (filename, corpusname, openersname):

    #files present, don't run
    if os.path.isfile(corpusname) and os.path.isfile(openersname):
        return

    data = urllib.request.urlopen(filename)
    textData = data.readlines()
    with open("fulltext.txt", 'w') as f:
        for l in textData:
            f.write(l.decode('utf-8'))
    data.close()
    wordVec = []
    for line in textData:
        wordList = line.decode('utf-8').strip().split(" "); #replace("\t", "")
        for w in wordList:
            if w.isupper():
                wordVec.append(w.capitalize().strip())
            else:
                wordVec.append(w.strip())

    corpus = { ("prefix","suffix") : [] }
    openers = []
    starter = False

    #establish corpus of empty lists TODO setdefault
    for x in range(0, len(wordVec)-2):
        corpus[(wordVec[x],wordVec[x+1])] = []

    #fill corpus
    for x in range(0, len(wordVec)-2):
        corpus[(wordVec[x],wordVec[x+1])].append(wordVec[x+2])
        if (starter):
            starter = False
            openers.append((wordVec[x], wordVec[x+1], wordVec[x+2]))
            continue
        if wordVec[x].endswith(('.','?','!',';') ):
            starter = True

    #serialize and store
    with open(corpusname, 'wb') as f:
        pickle.dump(corpus, f)
    with open(openersname, 'wb') as f:
        pickle.dump(openers, f)
    
    return


def findtxt(phrase):
    with open('fulltext.txt', 'r') as f:
        textData = f.read()
        if textData.find(phrase):
            return True
        else:
            return False

#generates a phrase using tweets upto 100 words long, or until punctuation
def genPhrase( corpusname, openersname ):
    
    #unpickle objects
    with open(corpusname, 'rb') as f:
        corpus = pickle.loads(f.read())
    with open(openersname, 'rb') as f:
        openers = pickle.loads(f.read())

    initKey = random.choice(openers)
    first = initKey[0].capitalize()
    second = initKey[1]
    third = initKey[2]

    sentence = []
    sentence.append(first)
    sentence.append(second)
    sentence.append(third)

    for x in range(0,100):
        first = second
        second = third
        initList = corpus[(first, second)]
        third = random.choice(initList)
        sentence.append(third)
        if len(third) > 0 and third.endswith(('.','?','!',';')) and len(third) > 2 and third != "Mr." and third != "Mrs.":
            break
   
    output = ""
    for w in sentence:
        output += " " + w.strip()
    output = output.lstrip()

    #check for matched quotations
    val = 0
    for c in output:
        if c == '"':
            val += 1
    if val%2 == 1:
        output += "\""

    

    return (output, findtxt(output), len(output))
