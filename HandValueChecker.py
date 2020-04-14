import PokerWidgets
import numpy as np

def returnBetterHand(hand1,hand2):
    i=0
    while i < len(hand1):
        if hand1[i] > hand2[i]:
            return 1
        if hand1[i] < hand2[i]:
            return 2
        i+=1
    return 0

def returnHandValueNewer(cards):
    return


def returnHandValueNew(cards):
    flush = flushOrStraightFlushCheck(cards)
    straight= straightCheck(cards)
    other= highCardThroughHouse(cards)
    flushval=flush[0]
    straightval=straight[0]
    otherval=other[0]
    firstValArray=np.array([flushval,straightval,otherval])
    maxIndex=np.argmax(firstValArray)
    if maxIndex==0:
        return flush
    if maxIndex==1:
        return straight
    else:
        return other

def straightCheck(cards): ## takes in unmodified cards
    cards = PokerWidgets.valueOfArrayIntegers(cards)
    cards = np.sort(cards, axis=None)
    cards = np.unique(cards, return_counts=True)
    organizedCards = cards[0][::-1]
    if organizedCards[0]==14:
        newOrganizedCards= np.zeros((len(organizedCards)+1))
        newOrganizedCards[len(organizedCards)]=1
        i=0
        while i < len(newOrganizedCards)-1:
            newOrganizedCards[i]=organizedCards[i-1]
            i+=1
        organizedCards=newOrganizedCards
    organizedCards=np.sort(organizedCards)[::-1]
    i=0
    while i < len(organizedCards)-4:
        j=0
        while j < 4:
            if organizedCards[i+j]-1==organizedCards[i+j+1]:
                j += 1
                if j == 4:
                    return np.array(
                        [5,organizedCards[i]])
            else:
                break
        i+=1
    return np.array([0])

def flushOrStraightFlushCheck(cards): ## takes in unmodified cards
    amountOfSuits=np.array([0,0,0,0])
    domsuit=""
    i=0
    while i < len(cards):
        if cards[i][0] == "♣":
            amountOfSuits[0]+=1
        elif cards[i][0] == "♡":
            amountOfSuits[1] += 1
        elif cards[i][0] == "♠":
            amountOfSuits[2] += 1
        else:
            amountOfSuits[3] += 1
        i+=1
    maxIndex=np.argmax(amountOfSuits)
    if amountOfSuits[maxIndex] <5:
        return [0] ## indicates no flush but did not check for straight
    elif np.argmax(amountOfSuits) ==0:
        domsuit="♣"
    elif np.argmax(amountOfSuits) ==1:
        domsuit="♡"
    elif np.argmax(amountOfSuits) ==2:
        domsuit="♠"
    else:
        domsuit="♢"
    arrayOfPotentialFlushCards=[]
    i=0
    while i < len(cards):
        if cards[i][0]== domsuit:
            arrayOfPotentialFlushCards.append(cards[i])
        i+=1
    straightResult = straightCheck(arrayOfPotentialFlushCards)
    arrayOfPotentialFlushCards=np.sort(PokerWidgets.valueOfArrayIntegers(arrayOfPotentialFlushCards),axis=None)[::-1]
    if straightResult[0] != 0:
        return np.array([9,straightResult[1]])
    returnArray = np.full((6,),0)
    returnArray[0]=6
    i=1
    while i < 6:
        returnArray[i] = arrayOfPotentialFlushCards[i-1]
        i+=1
    return returnArray

def highCardThroughHouse(cards): ## takes in unmodified cards
    cards = PokerWidgets.valueOfArrayIntegers(cards)
    cards=np.sort(cards,axis=None)
    cards=np.unique(cards, return_counts=True)
    cards_unique = cards[0]
    cards_unique = cards_unique[::-1]
    card_counts=cards[1]
    card_counts=card_counts[::-1]
    max_index= np.argmax(card_counts)
    maxInt=card_counts[max_index]
    if maxInt==1: ## deal with high card
        return np.array([1,cards_unique[0],cards_unique[1],cards_unique[2],cards_unique[3],cards_unique[4]])
    if maxInt==2: ## deal with pair and two pair
        listOfPairs=[]
        i=0
        while i < len(card_counts):  ## adding all pairs to a list
            if card_counts[i]==2:
                listOfPairs.append(cards_unique[i])
            i+=1
        if len(listOfPairs)== 1: ## if there is only one pair
            returnArray=[]
            returnArray.append(2)
            returnArray.append(listOfPairs[0])
            i=0
            iteration=0
            while i < 3:
                if cards_unique[iteration]!= listOfPairs[0]:
                    returnArray.append(cards_unique[iteration])
                    i+=1
                iteration+=1
            return np.array(returnArray)
        else:                    ## if multiple pairs are present
            returnArray=np.full((4,),0)
            returnArray[0] = 3
            returnArray[1] = listOfPairs[0]
            returnArray[2]= listOfPairs[1]
            iterator=0
            i=0
            while i <1:
                if cards_unique[iterator]!= returnArray[1] and cards_unique[iterator]!= returnArray[2]:
                    returnArray[3]= cards_unique[iterator]
                    i = 1
                iterator+=1
            return returnArray
    if maxInt==3: ## Trips and Boats
        listOfPairs = []
        i = 0
        while i < len(card_counts):  ## adding all pairs to a list
            if card_counts[i] == 2:
                listOfPairs.append(cards_unique[i])
            i += 1
        listOfTrips = []
        i = 0
        while i < len(card_counts):  ## adding all pairs to a list
            if card_counts[i] == 3:
                listOfTrips.append(cards_unique[i])
            i += 1
        if len(listOfPairs)==0 and len(listOfTrips)==1: #trips
            returnArray=np.array([4,listOfTrips[0],0,0])
            iterator=0
            i = 0
            while i < 2:
                if cards_unique[iterator] != listOfTrips[0]:
                    returnArray[2+i] = cards_unique[iterator]
                    i += 1
                iterator += 1
            return returnArray
        else:### Boats
            i=0
            while i < len(cards_unique):
                if cards_unique[i] != listOfTrips[0]:
                    if cards_unique[i] in listOfTrips or cards_unique[i] in listOfPairs:
                        return np.array([7, listOfTrips[0], cards_unique[i]])
                i+=1
    if maxInt==4: ## Quads
        quad=0
        i = 0
        while i < len(card_counts):  ## adding all pairs to a list
            if card_counts[i] == 4:
                quad =cards_unique[i]
                break
            i += 1
        i = 0
        while i < len(card_counts):  ## adding all pairs to a list
            if card_counts[i] != 4:
                return np.array([8,quad,cards_unique[i]])
            i+=1

