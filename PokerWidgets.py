import math
import numpy as np
def deckOfCards(): ## Working
    v= np.array(["♣A", "♣K", "♣Q", "♣J", "♣T","♣9","♣8","♣7","♣6","♣5","♣4","♣3","♣2","♢A","♢K","♢Q","♢J","♢T","♢9","♢8","♢7","♢6","♢5","♢4","♢3","♢2","♡A","♡K","♡Q","♡J","♡T","♡9","♡8","♡7","♡6","♡5","♡4","♡3","♡2","♠A", "♠K", "♠Q","♠J","♠T","♠9","♠8","♠7","♠6","♠5","♠4","♠3","♠2"])
    return v

def valueOf(cardNotSuit): ## Working
    if cardNotSuit == "A":
        return 14
    if cardNotSuit == "K":
        return 13
    if cardNotSuit == "Q":
        return 12
    if cardNotSuit == "J":
        return 11
    if cardNotSuit == "T":
        return 10
    else:
        return int(cardNotSuit)

def allHandsConverted(): ## Working
    v=np.array(["uAA",
    "uKK",
    "uQQ",
    "uJJ",
    "uTT",
    "sAK",
    "sAQ",
    "u99",
    "sKQ",
    "uAK",
    "sAJ",
    "sKJ",
    "sAT",
    "uAQ",
    "u88",
    "sQJ",
    "sKT",
    "uKQ",
    "sQT",
    "uAJ",
    "sJT",
    "sA9",
    "u77",
    "sA5",
    "uKJ",
    "uAT",
    "sK9" ,
    "sA8" ,
    "uQJ",
    "sQ9",
    "sA7",
    "uKT",
    "sJ9",
    "u66",
    "sT9",
    "uQT",
    "sK8",
    "sA6",
    "sA4",
    "uJT",
    "sA3",
    "sK7",
    "sQ8",
    "sA2",
    "u55",
    "uA9",
    "sJ8",
    "sT8",
    "sK6",
    "s98",
    "uK9",
    "uA8",
    "sK5",
    "sQ7",
    "u44",
    "uQ9",
    "sK4",
    "uJ9",
    "sJ7",
    "uA7",
    "sT7",
    "s97",
    "s87",
    "sQ6",
    "sK3",
    "sK2",
    "uA5",
    "sQ5",
    "u33",
    "uK8",
    "uA6",
    "uA4",
    "s76",
    "uA3",
    "sQ3",
    "sT6",
    "sJ5",
    "sQ4",
    "sJ6",
    "u22",
    "s86",
    "s96",
    "uQ8",
    "uK7",
    "uJ8",
    "sQ2",
    "uT9",
    "s65",
    "u98",
    "uA2",
    "sJ4",
    "uK6",
    "s75",
    "sJ3",
    "s85",
    "s54",
    "sT5",
    "uK5",
    "sJ2",
    "s95",
    "sT4",
    "s64",
    "uQ7",
    "u97",
    "u87",
    "uJ7",
    "uT8",
    "uK4",
    "uT7",
    "sT3",
    "s74",
    "s53",
    "uK3",
    "uQ6",
    "s84",
    "sT2",
    "s94",
    "uK2",
    "s43",
    "s63",
    "uQ5",
    "s93",
    "u76",
    "u86",
    "s92",
    "s73",
    "s52",
    "uQ4",
    "uT6",
    "s83",
    "uJ6",
    "u96",
    "uQ3",
    "u65",
    "s82",
    "s42",
    "uQ2",
    "s62",
    "s32",
    "uJ5",
    "u75",
    "s72",
    "uJ4",
    "u54",
    "u85",
    "uJ3",
    "uT5",
    "u95",
    "uJ2",
    "u64",
    "uT4",
    "u53",
    "u74",
    "uT3",
    "u84",
    "uT2",
    "u43",
    "u94",
    "u63",
    "u93",
    "u52",
    "u73",
    "u92",
    "u42",
    "u83",
    "u32",
    "u82",
    "u62",
    "u72"])
    return v

def valueOfArrayIntegers(array): ## Working
    arrayOfJustNumbers = np.zeros((len(array),1))
    i=0
    while i< len(array):
        v = array[i]
        v=v[1]
        arrayOfJustNumbers[i]= valueOf(v)
        i+=1
    return arrayOfJustNumbers

def valueOfArraySuits(array): ## Working
    returnArray = np.full([len(array), 1], "a")
    i=0
    while i< len(array):
        v = array[i]
        v=v[0]
        returnArray[i]= v
        i+=1
    return returnArray

def convertToCharacterForm(myCard1, myCard2):  ## Working
    myHand=""
    if valueOf(myCard1[1]) < valueOf(myCard2[1]):
        c1 = myCard1
        c2 = myCard2
        myCard1 = c2
        myCard2 = c1
    if myCard1[0] == myCard2[0]:
        myHand = myHand + ("s")
    if myCard1[0] != myCard2[0]:
        myHand = myHand + ("u")
    myHand = myHand + (myCard1[1])
    myHand= myHand + (myCard2[1])
    return myHand

def convertArrayOfHandsToCharacterForm(array): ###Working
    returnArray = np.full([len(array), 1], "aaa")
    i=0
    while i < len(array):
        print(array[i,0])
        print(array[i,1])
        returnArray[i] = convertToCharacterForm(array[i,0],array[i,1])
        i+=1
    return returnArray

def shuffledDeck():   ## Working
    v = deckOfCards()
    np.random.shuffle(v)
    return v

def randomHandsAndCommunityCards(players): ## Working
    v=shuffledDeck()
    returnArray = np.full([players, 2], "aaa")
    i=0
    j=0
    while i < len(returnArray):
        returnArray[i,0] = v[j]
        returnArray[i,1] = v[j+1]
        j+=2
        i+=1
    arrayOfCommunityCards  = np.full([5, 1], "aaa")
    i=0
    while i <5:
        arrayOfCommunityCards[i,0]= v[((players*2)+i)]
        i+=1
    return [returnArray,arrayOfCommunityCards]

def convertArrayOfHandsTo1DArray(array): ## Working
    array=np.reshape(array,(len(array)*2))
    return array

def runoutPermutationGenerator(): ## produces a file with all the permutations of runouts
    base_array=deckOfCards()
    f= open("allCombinationsOfRunoutsWithDuplicates.txt","w+",encoding='utf-8') ## Wrong, needs fixing
    a=-1
    b=0
    c=0
    d=0
    e=0
    while a < 51:
        a+=1
        print(a)
        b=0
        c=0
        d=0
        e=0
        if are_not_duplicates(np.array([a, b, c, d, e])):
            f.write(base_array[a]+base_array[b]+base_array[c]+base_array[d]+base_array[e]+'\n')
        initializing_varible=1
        initializing_varible2=1
        initializing_varible3=1
        while b < 51:
            if(initializing_varible==0):
                b+=1
                c=0
                d=0
                e=0
                initializing_varible2=1
                initializing_varible3=1
                if are_not_duplicates(np.array([a, b, c, d, e])):
                    f.write(base_array[a]+base_array[b]+base_array[c]+base_array[d]+base_array[e]+'\n')
            while c < 51:
                if(initializing_varible==0 and initializing_varible2==0):
                    c+=1
                    d=0
                    e=0
                    initializing_varible3=1
                    if are_not_duplicates(np.array([a, b, c, d, e])):
                        f.write(base_array[a]+base_array[b]+base_array[c]+base_array[d]+base_array[e]+'\n')
                while d < 51:
                    if(initializing_varible==0 and initializing_varible2==0 and initializing_varible3==0):
                        d+=1
                        e=0
                        if are_not_duplicates(np.array([a, b, c, d, e])):
                            f.write(base_array[a]+base_array[b]+base_array[c]+base_array[d]+base_array[e]+'\n')
                    if(initializing_varible==1):
                        initializing_varible=0
                    if initializing_varible2==1:
                        initializing_varible2=0
                    if initializing_varible3==1:
                        initializing_varible3=0
                    while e < 51:
                        e+=1
                        if are_not_duplicates(np.array([a, b, c, d, e])):
                            f.write(base_array[a]+base_array[b]+base_array[c]+base_array[d]+base_array[e]+'\n')
    f.close()

def runoutCombinationsGenerator(): ## Up to 4
    f= open("allCombinationsOfRunouts.txt","w+",encoding='utf-8')
    array1=deckOfCards()
    array2=np.full([51,],"aa")
    i=0
    while i < len(array2):
        array2[i]=array1[i+1]
        i+=1
    array3=np.full([50,],"aa")
    i=0
    while i < len(array3):
        array3[i]=array1[i+2]
        i+=1
    array4=np.full([49,],"aa")
    i=0
    while i < len(array4):
        array4[i]=array1[i+3]
        i+=1
    array5=np.full([48,],"aa")
    i=0
    while i < len(array5):
        array5[i]=array1[i+4]
        i+=1
    init =0
    init2=0
    init3=0
    a=-1
    b=-1
    c=-1
    d=-1
    e=0
    while a < len(array1):
        print(a)
        a+=1
        b=a
        init3=0
        while b < len(array2):
            if init3==1:
                b+=1
            c=b
            init3=1
            init2=0
            while c < len(array3):
                if init2 ==1:
                    c+=1
                d=c
                init2=1
                init=0
                while d <len(array4):
                    if init ==1:
                        d+=1
                    e=d
                    init =1
                    while e < len(array5):
                        f.write(array1[a]+array2[b]+array3[c]+array4[d]+array5[e]+'\n')
                        e+=1
    f.close()

def allHandsGenerator():
    f= open("allStartingHands.txt","w+",encoding='utf-8')
    deck = deckOfCards()
    i=-1
    j=0
    while i <len(deck):
        i+=1
        j=i+1
        while j < len(deck):
            f.write(deck[i]+deck[j]+'\n')
            j+=1
    f.close()

def are_not_duplicates(array):
    i=0
    while i < len(array):
        j=1
        while i + j < len(array):
            if array[i+j]== array[i]:
                return False
            j+=1
        i+=1
    return True

def combinationGeneraor(n,k): ## n is total, k is number of items
        return math.factorial(n)/(math.factorial(k)*(math.factorial(n-k)))


def blocks(files, size=65536):
        while True:
            b = files.read(size)
            if not b: break
            yield b

def combinationDictionaryNumerical():
    all_Combinations=  open("allCombinationsOfRunouts.txt","r",encoding='utf-8')
    returnArray=np.full((2598960,5),"aa")
    i=0
    while i < 2598960:
        all_Combinations_line = all_Combinations.readline()[0:10]
        returnArray[i][0]=all_Combinations_line[0:2]
        returnArray[i][1]=all_Combinations_line[2:4]
        returnArray[i][2]=all_Combinations_line[4:6]
        returnArray[i][3]=all_Combinations_line[6:8]
        returnArray[i][4]=all_Combinations_line[8:]
        i+=1
    all_Combinations.close()
    return returnArray

def allHandsDictionaryNumerical():
    all_hands=  open("allStartingHands.txt","r",encoding='utf-8')
    returnArray=np.full((1326,2),"aa")
    i=0
    while i < 2598960:
        all_hands_line = all_hands.readline()[0:10]
        returnArray[i][0]=all_hands_line[0:2]
        returnArray[i][1]=all_hands_line[2:4]
        i+=1
    all_hands.close()
    return returnArray



