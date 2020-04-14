import numpy as np
import pickle
import HandValueChecker
import PokerWidgets
import SimulateHand
import os.path
from datetime import datetime

def allRunoutsPickleConversion():
    v=PokerWidgets.combinationDictionaryNumerical()
    file1_pickle = open("allCombinatiosOfRunouts.pickle", "wb")
    pickle.dump(v, file1_pickle, pickle.HIGHEST_PROTOCOL)
    file1_pickle.close()

def allHandsPickle():
    returnArray= np.full((1326,2),"aa")
    all_hands=  open("allStartingHands.txt","r",encoding='utf-8')
    i=0
    while i < 1326:
        allHandsLine=all_hands.readline()
        returnArray[i][0]= allHandsLine[0:2]
        returnArray[i][1] = allHandsLine[2:5]
        i+=1
    all_hands.close()
    file1_pickle = open("allHands.pickle", "wb")
    pickle.dump(returnArray, file1_pickle, pickle.HIGHEST_PROTOCOL)
    file1_pickle.close()



def allRunoutsByHandToPickle(name): ## Pickle of the array which contains the value of every single runout for a hand
    array = np.full((2598960,6),0)
    h2file = open("allCombinatiosOfRunouts.pickle", "rb")
    allHands = pickle.load(h2file)
    h2file.close()
    i=0
    while i < 2598960:
            cards= np.array([name[0:2],name[2:4],allHands[i][0],allHands[i][1],allHands[i][2],allHands[i][3],allHands[i][4]])
            if PokerWidgets.are_not_duplicates(cards)== True:
                cardValue = HandValueChecker.returnHandValueNew(cards)
                j=0
                while j < len(cardValue):
                    array[i][j]= cardValue[j]
                    j+=1
            i+=1
    v="D:\AllValuesByHand\AllRunoutsByHandPickle\\"
    file1_pickle = open(v+name+"Values.pickle", "wb")
    pickle.dump(array,file1_pickle,pickle.HIGHEST_PROTOCOL)
    file1_pickle.close()

def allRunoutsByHandPickleFull(number): ## performs allRunoutsByHandToPickle on every hand
    i=number
    file1_pickle = open("allHands.pickle", "rb")
    allHands = pickle.load(file1_pickle)
    file1_pickle.close()
    while i < 1326:
        print(i)
        name=allHands[i][0]+allHands[i][1]
        allRunoutsByHandToPickle(name)
        i+=1

# def fillInallRunoutsByHandPickleFullTest():
#     i = 0
#     file1_pickle = open("allHands.pickle", "rb")
#     allHands = pickle.load(file1_pickle)
#     file1_pickle.close()
#     while i < 1326:
#         print(i)
#         name = allHands[i][0] + allHands[i][1]
#         print(name)
#         testName="D:\AllValuesByHand\AllRunoutsByHandPickle\\" + name+'Values.pickle'
#         asdf = open(testName, "rb")
#         asdf.close()
#         print(testName)
#         i += 1

def handAllPreWinPercentages(hand): ###1st cell, base hand wins, 2nd cell loses, 3rd cell ties
    c1=hand[0:2]
    c2=hand[2:4]
    i = 0
    file1_pickle = open("allHands.pickle", "rb")
    allHands = pickle.load(file1_pickle)
    file1_pickle.close()
    dumpArray = np.full((1326,3), 00.00000000000000000)
    i=0
    while i < 1326:
        print(i)
        currHand=[allHands[i][0],allHands[i][1]]
        if c1 and c2 not in currHand:
            v=SimulateHand.two_hands_theoretical_by_pickle(hand,str(currHand[0]+currHand[1]))
            dumpArray[i][0]=v[0]
            dumpArray[i][1]=v[1]
            dumpArray[i][0] = v[2]
        i+=1
    v = "D:\AllValuesByHand\AllHandsPrePercentages\\"
    file1_pickle = open(+hand+ "PrePercentagesValues.pickle", "wb")
    pickle.dump(dumpArray, file1_pickle, pickle.HIGHEST_PROTOCOL)
    file1_pickle.close()

def handAllPreWinPercentagesRounded(hand): ###1st cell, base hand wins, 2nd cell loses, 3rd cell ties
    c1=hand[0:2]
    c2=hand[2:4]
    i = 0
    file1_pickle = open("allHands.pickle", "rb")
    allHands = pickle.load(file1_pickle)
    file1_pickle.close()
    dumpArray = np.full((1326,3), 00.00000000000000000)
    i=0
    while i < 1326:
        currHand=[allHands[i][0],allHands[i][1]]
        if c1 and c2 not in currHand:
            v=SimulateHand.two_hands_theoretical_by_pickle_rounding(hand,str(currHand[0]+currHand[1]))
            dumpArray[i][0]=v[0]
            dumpArray[i][1]=v[1]
            dumpArray[i][2] = v[2]
        i+=1
    v = "D:\AllValuesByHand\AllHandsPrePercentages\\"
    file1_pickle = open(v+hand+ "PrePercentagesRoundedValues.pickle", "wb")
    pickle.dump(dumpArray, file1_pickle, pickle.HIGHEST_PROTOCOL)
    file1_pickle.close()

# allRunoutsByHandPickleFull(0)