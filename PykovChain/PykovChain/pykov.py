#Python Markov Chain generator for 2-word order chains
#author: Morgan Osborn

#currently build map per use, NOTGOOD

#TODO, fill pairs last array, make sure no empty strings anywhere, format into actual sentence

import random


#generates corpus and TODO generates opening phrases by ref
def genCorpus (filename, openers):
    with open(filename) as file:
        textData = file.readlines()
        wordVec = []
    for line in textData:
        wordList = line.strip().split(" ");
        for w in wordList:
            if w.isupper():
                wordVec.append(w.capitalize())
            else:
                wordVec.append(w)

    corpus = { ("prefix","suffix") : [] }

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


    return corpus

#generates a phrase using tweets upto 100 words long, or until punctuation
def genPhrase( corpus, openers ):
    
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
        output += " " + w
    output = output.lstrip()

    #check for matched quotations
    val = 0
    for c in output:
        if c == '"':
            val += 1
    if val%2 == 1:
        output += "\""

    return output
