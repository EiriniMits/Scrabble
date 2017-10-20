from mylib import *
import pickle

# @author Eirini Mitsopoulou

#-------------------------------Run this file---------------------------------

def createGreek7():
    filename = "greek.txt"
    filename2 = "greek7.txt"
    inFile = open(filename, 'r',encoding='UTF8')
    outFile = open(filename2, 'w',encoding='UTF8')
    for line in inFile:
        if len(line) <=8 and len(line) >2:
            outFile.write(line)
    outFile.close()
    inFile.close()


def loadWords(sac):
    filename = "greek7.txt"
    inFile = open(filename, 'r',encoding='UTF8')
    wordDict = {}
    for line in inFile:
        line = line.strip('\n')
        score = sac.getWordScore(line)
        wordDict[line] = wordDict.get(line, 0) + score
    return wordDict


if __name__ == '__main__':
    createGreek7()
    sac = SakClass()
    wordDict = loadWords(sac)
    file_Name = "greek7.pkl"
    with open(file_Name,'wb') as f:
        pickle.dump(wordDict,f)
