import HandValueChecker
import PokerWidgets
import numpy as np
def test_highCard():
    communityCards = np.array(['♢Q', '♢K', '♢8', '♣5', '♡J'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[1,13,12,11,8,5]
    i=0
    while i < 6:
        assert v[i]==compared[i]
        i+=1
    communityCards = np.array(['♢Q', '♢K', '♢8', '♣5', '♢J', '♣6', '♡T'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[1,13,12,11,10,8]
    i=0
    while i < 6:
        assert v[i]==compared[i]
        i+=1

def test_pair():
    communityCards = np.array(['♢Q', '♢K', '♢8', '♣K', '♡J'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[2,13,12,11,8]
    i=0
    while i < 5:
        assert v[i]==compared[i]
        i+=1
    communityCards = np.array(['♢Q', '♢K', '♢8', '♣K', '♡J','♣A', '♡2'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[2,13,14,12,11]
    i=0
    while i < 5:
        assert v[i]==compared[i]
        i+=1

def test_twoPair():
    communityCards = np.array(['♢Q', '♢K', '♢8', '♣K', '♡Q'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[3,13,12,8]
    i=0
    while i < 4:
        assert v[i]==compared[i]
        i+=1
    communityCards = np.array(['♢Q', '♢K', '♢2', '♣2', '♡9', '♡K', '♡Q'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[3,13,12,9]
    i=0
    while i < 4:
        assert v[i]==compared[i]
        i+=1

def test_trips():
    communityCards = np.array(['♢Q', '♢K', '♢8', '♣K', '♡K',"♢2"])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[4,13,12,8]
    i=0
    while i < 4:
        assert v[i]==compared[i]
        i+=1
    communityCards = np.array(['♢Q', '♢K', '♢8', '♣K', '♡K', '♡3', '♢2'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[4,13,12,8]
    i=0
    while i < 4:
        assert v[i]==compared[i]
        i+=1

def test_straight(): ## Needs to have ace be 1 or 14
    communityCards = np.array(['♢Q', '♢K', '♠A', '♣J', '♡T','♡2'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[5,14]
    i=0
    while i < 2:
        assert v[i]==compared[i]
        i+=1
    communityCards = np.array([ '♠A', '♣3', '♡2','♡3','♡5','♡4','♣5'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[5,5]
    i=0
    while i < 2:
        assert v[i]==compared[i]
        i+=1

    communityCards = np.array(['♠6', '♣3', '♡2', '♡3', '♡5', '♡4', '♣5'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared = [5, 6]
    i = 0
    while i < 2:
        assert v[i] == compared[i]
        i += 1

def test_flush():
    communityCards = np.array(['♢Q', '♢K', '♢A', '♢J', '♢8','♣8','♣T'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[6,14,13,12,11,8]
    i=0
    while i < 6:
        assert v[i]==compared[i]
        i+=1

def test_fullhouse():
    communityCards = np.array(["♣A","♣T","♣K","♣Q","♢K","♢Q","♡K"])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[7,13,12]
    i=0
    while i < 3:
        assert v[i]==compared[i]
        i+=1
    communityCards = np.array(['♢K', '♠A', '♢A', '♠Q', '♣Q', '♠K', '♣K'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[7,13,14]
    i=0
    while i < 3:
        assert v[i]==compared[i]
        i+=1

def test_quads():
    communityCards = np.array(['♢Q', '♢K', '♠K', '♣K', '♡K'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[8,13,12]
    i=0
    while i < 3:
        assert v[i]==compared[i]
        i+=1
    communityCards = np.array(['♢A', '♢K', '♠K', '♣K', '♡K','♣A', '♠A'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[8,13,14]
    i=0
    while i < 3:
        assert v[i]==compared[i]
        i+=1

def test_striaghtflush():
    communityCards = np.array(['♢A', '♢K', '♢Q', '♢J', '♢T','♢9'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[9,14]
    i=0
    while i < 2:
        assert v[i]==compared[i]
        i+=1
    communityCards = np.array([ '♡A', '♣J', '♡2','♡3','♡4','♡5','♣J'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared =[9,5]
    i=0
    while i < 2:
        assert v[i]==compared[i]
        i+=1
    communityCards = np.array(['♡6', '♣J', '♡2', '♡3', '♡4', '♡5', '♣J'])
    v = HandValueChecker.returnHandValueNew(communityCards)
    compared = [9, 6]
    i = 0
    while i < 2:
        assert v[i] == compared[i]
        i += 1

def testWinPercentage(k): ## Seems to Be working +/- 0.001
    hand1Cards= np.array(["♡A",'♣2'])
    hand2Cards= np.array(['♡K','♡9'])
    deck = PokerWidgets.deckOfCards()
    deck= np.delete(deck, np.argwhere(deck==hand1Cards[0]))
    deck= np.delete(deck, np.argwhere(deck==hand1Cards[1]))
    deck= np.delete(deck, np.argwhere(deck==hand2Cards[0]))
    deck= np.delete(deck, np.argwhere(deck==hand2Cards[1]))
    hand1=0
    hand2=0
    ties=0
    i=0
    while i < k: # v should be 61
        print(i)
        np.random.shuffle(deck)
        handOne= np.array([hand1Cards[0],hand1Cards[1],deck[0],deck[1],deck[2],deck[3],deck[4]])
        hand1Value= HandValueChecker.returnHandValueNew(handOne)
        handTwo=np.array([hand2Cards[0],hand2Cards[1],deck[0],deck[1],deck[2],deck[3],deck[4]])
        hand2Value= HandValueChecker.returnHandValueNew(handTwo)
        v= HandValueChecker.returnBetterHand(hand1Value,hand2Value)
        if v ==0:
            ties+=1
        if v == 1:
            hand1+=1
        if v==2:
            hand2+=1
        i+=1
    v= hand1/(hand1+hand2+ties)
    print(v)
    print(hand2/(hand1+hand2+ties))
    print(ties/(hand1+hand2+ties))



def testAll():  ## Need conflicting hands 5-7
    print("0")
    test_highCard()
    print("1")
    test_pair()
    print("2")
    test_twoPair()
    print("3")
    test_trips()
    print("4")
    test_quads()
    print("5")
    test_straight()
    print("6")
    test_flush()
    print("7")
    test_fullhouse()
    print("8")
    test_striaghtflush()
    print("9")
    testWinPercentage(1000000)
