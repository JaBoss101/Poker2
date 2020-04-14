import PokerWidgets as pw
import HandValueChecker
import random
import numpy as np
import os
from datetime import datetime
import pickle

def two_hands_theoretical_by_pickle(name1,name2): ## Takes in pickled files
    h1wins=0
    h2wins=0
    ties=0
    h1= "D:\AllValuesByHand\AllRunoutsByHandPickle\\" + name1 + 'Values.pickle'
    h2= "D:\AllValuesByHand\AllRunoutsByHandPickle\\" + name2 + 'Values.pickle'
    h1file=open(h1, "rb")
    h2file=open(h2, "rb")
    h3file=open("allCombinatiosOfRunouts.pickle","rb")
    h1Hands= pickle.load(h1file)
    h2Hands= pickle.load(h2file)
    h2file.close()
    h1file.close()
    i=0
    while i < 2598960:
        currH1=h1Hands[i]
        currH2=h2Hands[i]
        if currH1[0] != 0 and currH2[0] != 0:
            v = HandValueChecker.returnBetterHand(currH1, currH2)
            if v == 0:
                ties += 1
            if v == 1:
                h1wins += 1
            if v == 2:
                h2wins += 1
        i+=1
    return np.array([(h1wins/ (h1wins+ties+h2wins)),(h2wins/ ((h1wins+ties+h2wins))),(ties/(h1wins+ties+h2wins))])

def two_hands_theoretical_by_pickle_rounding(name1,name2): ## Takes in pickled files
    h1wins=0
    h2wins=0
    ties=0
    h1= "D:\AllValuesByHand\AllRunoutsByHandPickle\\" + name1 + 'Values.pickle'
    h2= "D:\AllValuesByHand\AllRunoutsByHandPickle\\" + name2 + 'Values.pickle'
    h1file=open(h1, "rb")
    h2file=open(h2, "rb")
    h3file=open("allCombinatiosOfRunouts.pickle","rb")
    h1Hands= pickle.load(h1file)
    h2Hands= pickle.load(h2file)
    h2file.close()
    h1file.close()
    i=0
    while i < 2598960:
        currH1=h1Hands[i]
        currH2=h2Hands[i]
        if currH1[0] != 0 and currH2[0] != 0:
            v = HandValueChecker.returnBetterHand(currH1, currH2)
            if v == 0:
                ties += 1
            if v == 1:
                h1wins += 1
            if v == 2:
                h2wins += 1
        i+=1
    return np.array([round((h1wins/ (h1wins+ties+h2wins)),4),round((h2wins/ ((h1wins+ties+h2wins))),4),round(((ties)/(h1wins+ties+h2wins)),4)])

def two_hands_theoretical_by_pickle_test(name1,name2): ## Takes in pickled files
    h1wins=0
    h2wins=0
    ties=0
    h1= "D:\AllValuesByHand\AllRunoutsByHandPickle\\" + name1 + 'Values.pickle'
    h2= "D:\AllValuesByHand\AllRunoutsByHandPickle\\" + name2 + 'Values.pickle'
    h1file=open(h1, "rb")
    h2file=open(h2, "rb")
    h3file=open("allCombinationsOfRunouts.txt","r", encoding='utf-8')
    h1Hands= pickle.load(h1file)
    h2Hands= pickle.load(h2file)
    h2file.close()
    h1file.close()
    high = 0
    pair = 0
    twoPair = 0
    threeOfAKind = 0
    straight = 0
    flush = 0
    fullHouse = 0
    Quads = 0
    straightFlush = 0
    i=0
    while i < 2598960:
        readline=h3file.readline()
        currH1=h1Hands[i]
        currH2=h2Hands[i]
        if currH1[0] != 0 and currH2[0] != 0:
            v = HandValueChecker.returnBetterHand(currH1, currH2)
            if v == 0:
                h1Hand=currH1[0]
                if h1Hand == 1:
                    high += 1
                if h1Hand == 2:
                    pair += 1
                if h1Hand == 3:
                    twoPair += 1
                if h1Hand == 4:
                    threeOfAKind += 1
                if h1Hand == 5:
                    straight += 1
                if h1Hand == 6:
                    flush += 1
                if h1Hand == 7:
                    print(name1 + readline[0:10])
                    print(currH1)
                    print(name2 + readline[0:10])
                    print(currH2)
                    fullHouse += 1
                if h1Hand == 8:
                    Quads += 1
                if h1Hand == 9:
                    straightFlush += 1
                ties += 1
            if v == 1:
                h1wins += 1
            if v == 2:
                h2wins += 1
        i+=1
    h3file.close()
    total=high+pair+twoPair+threeOfAKind+straight+flush+fullHouse+Quads+straightFlush
    print("high card" + str(high / total))
    print("pair" + str(pair / total))
    print("two pair" + str(twoPair / total))
    print("trips" + str(threeOfAKind / total))
    print("straight " + str(straight / total))
    print("flush" + str(flush / total))
    print("full house" + str(fullHouse / total))
    print(" quads" + str(Quads / total))
    print(" straight flush" + str(straightFlush / total))
    print(ties)
    print(str(ties+h1wins+h2wins))
    return np.array([((h1wins+(ties/2))/ (h1wins+ties+h2wins)),(h2wins+(ties/2))/ ((h1wins+ties+h2wins)),(ties/(h1wins+ties+h2wins))])

def checkHandContents():
    h1 = "D:\AllValuesByHand\AllRunoutsByHandPickle\\" + "♡9♠K" + 'Values.pickle'
    h1file=open(h1, "rb")
    h1Hands= pickle.load(h1file)
    h1file.close()
    high=0
    pair=0
    twoPair=0
    threeOfAKind=0
    straight=0
    flush=0
    fullHouse=0
    Quads=0
    straightFlush=0
    i=0
    while i < 2598960:
        h1Hand=h1Hands[i][0]
        if h1Hand==1:
            high+=1
        if h1Hand==2:
            pair+=1
        if h1Hand==3:
            twoPair+=1
        if h1Hand==4:
            threeOfAKind+=1
        if h1Hand==5:
            straight+=1
        if h1Hand==6:
            flush+=1
        if h1Hand==7:
            fullHouse+=1
        if h1Hand==8:
            Quads+=1
        if h1Hand==9:
            straightFlush+=1
        i+=1
    total=high+pair+twoPair+threeOfAKind+straight+flush+fullHouse+Quads+straightFlush
    print(total)
    print("high card"+ str(high/total))
    print("pair"+ str(pair/total))
    print("two pair"+ str(twoPair/total))
    print("trips"+ str(threeOfAKind/total))
    print("straight "+ str(straight/total))
    print("flush"+ str(flush/total))
    print("full house"+ str(fullHouse/total))
    print(" quads"+ str(Quads/total))
    print(" straight flush"+ str(straightFlush/total))

