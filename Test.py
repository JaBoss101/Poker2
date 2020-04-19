import toPickle
import pickle
i=1000
file1_pickle = open("D:\AllValuesByHand\AllHandsPrePercentages\♣2♢TPrePercentagesValues.pickle", "rb")
allHandsValues=pickle.load(file1_pickle)
file1_pickle.close()
print(allHandsValues[0])

