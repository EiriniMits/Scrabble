import random
import itertools


# @author Eirini Mitsopoulou


class SakClass:

    def __init__(self):
        self.letterValues = {'Α': 1, 'Β': 8, 'Γ': 4, 'Δ': 4, 'Ε': 1, 'Ζ': 10, 'Η': 1, 'Θ': 10, 'Ι': 1, 'Κ': 2, 'Λ': 3, 'Μ': 3, 'Ν': 1, 'Ξ': 10, 'Ο': 1, 'Π': 2, 'Ρ': 2, 'Σ': 1, 'Τ': 1, 'Υ': 2, 'Φ': 8, 'Χ': 8, 'Ψ': 10, 'Ω': 3}
        self.letters = { 'Α': 12, 'Β': 1, 'Γ': 2, 'Δ': 2, 'Ε': 8, 'Ζ': 1, 'Η': 7, 'Θ': 1, 'Ι': 8, 'Κ': 4, 'Λ': 3, 'Μ': 3, 'Ν': 6, 'Ξ': 1, 'Ο': 9, 'Π': 4, 'Ρ': 5, 'Σ': 7, 'Τ': 8, 'Υ': 4, 'Φ': 1, 'Χ': 1, 'Ψ': 1, 'Ω': 3}
        self.letters_in_sak = 102
        self.numOfLetters = 7


    def removeRandomLetters(self, hand, n):
        if self.letters_in_sak >= n:
            for i in range(n):
                tile = random.choice(list(self.letters.keys()))
                flag = 0
                while flag == 0:
                    if self.letters[tile]==0:
                        tile = random.choice(list(self.letters.keys()))
                    else:
                        self.letters[tile] -= 1
                        hand[tile] = hand.get(tile, 0) + 1
                        flag = 1
        return hand
                        
                        
    def findNotUsedLetters(self, hand, word):
        lword = list(word)
        for i in word:
            if hand.get(i,0) > 1:
                hand[i] = hand.get(i, 0) - 1
            else:
                del hand[i]
        return hand


    def putBackLetters(self,hand):
            for i in hand.keys():
                for j in range(hand[i]):
                    self.letters[i] += 1


    def displayLetters(self,hand):
        for letter in hand.keys():
            for j in range(hand[letter]):
                print(letter+ ','+str(self.letterValues[letter])+ '  ' ,end=" ")
        print()
    

    def getWordScore(self,word):
        wordScore = 0
        for i in word:
            wordScore += self.letterValues[i]
        return wordScore



class Game:
    
    def __init__(self):
        self.mytotalpoints = 0
        self.comptotalpoints = 0
    

    def isValidWord(self,word, hand, wordList):
        newHand = dict(hand)
        result = True
        
        #test if the letters of the word are accepted
        for i in word:
            if newHand.get(i,0) >= 1:
                newHand[i] -= 1
                result = True
            else:
                result = False
                break
        #Test if the word exists in calolog of accepted words
        if word in wordList and result == True:
            result = True
        else:
            result = False
        return result


    def results(self):
        winner = 1
        print('--------------')
        print('*ΑΠΟΤΕΛΕΣΜΑΤΑ*')
        print('--------------')
        print('Το σκορ σου: '+  str(self.mytotalpoints))
        print('To σκορ του H/Y: '+ str(self.comptotalpoints))
        if self.mytotalpoints > self.comptotalpoints:
            print('Νίκησες! Μπράβο !!!')
        elif self.mytotalpoints < self.comptotalpoints:
            print('Νικητής ο Η/Υ. Την επόμενη φορά θα τα πας καλύτερα.')
            winner = 2
        else:
            print('Ισοπαλία.')
            winner = 3
        print('---------------------------------------------------------')
        return winner



class Algorithm:
    
    def __init__(self):
        self.algorithm = 1

    def smartLetters(self, hand, wordDict, n):
        bestScore = 0
        bestWord = None
        s=self.convertToString(hand)
        s2=''
        
        for L in range(2, len(s)+1):
            for subset in itertools.permutations(s,L):
                s2 = ''.join(subset)
                if s2 in wordDict:
                    score = wordDict[s2]
                    if (score > bestScore):
                        bestScore = score
                        bestWord = s2
        
        return bestWord


    def minLetters(self,hand, wordDict, n):
        bestScore = 0
        bestWord = None
        s=self.convertToString(hand)
        s2=''
        for L in range(2, len(s)+1):
            if bestWord != None:
                break
            for subset in itertools.permutations(s,L):
                s2 = ''.join(subset)
                if s2 in wordDict:
                    bestWord = s2
        
        return bestWord



    def maxLetters(self,hand, wordDict, n):
        bestScore = 0
        bestWord = None
        s=self.convertToString(hand)
        s2=''
        for L in range(len(s), 1,-1):
            if bestWord != None:
                break
            for subset in itertools.permutations(s,L):
                s2 = ''.join(subset)
                if s2 in wordDict:
                    bestWord = s2

        return bestWord
    
    
    def convertToString(self,hand):
        s=''
        newHand = dict(hand)
        for i in hand.keys():
            while newHand.get(i,0) >= 1:
                newHand[i] -= 1
                s = s + i
        return s


