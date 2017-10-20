from mylib import *
import pickle
import time

# @author Eirini Mitsopoulou



#-------------------------------Run this file---------------------------------

def saveInFile(g, winner, score):   
    scoreList = []
    scoreList.append("Παιχνίδι:   Hμερομηνία:" + time.strftime("%d/%m/%Y  ")+"'Ωρα: "+time.strftime("%H:%M:%S"))
    scoreList.append('--------------------------------------------------------')
    if winner == 1:
        scoreList.append('-> Νίκησες! <-')
    elif winner == 2:
        scoreList.append('-> Νικητής ο Η/Υ <-')
    else:
        scoreList.append('-> Ισοπαλία <-')
    scoreList.append('- Το τελικό σκορ σου:     '+  str(g.mytotalpoints))
    scoreList.append('- To τελικό σκορ του H/Y: '+  str(g.comptotalpoints))
    scoreList.append('---------------------------------------------------------')
    scoreList.append('**** Αναλυτικά Αποτελέσματα και Κινήσεις ****')
    scoreList.append('---------------------------------------------------------')
    for key in score:
        l=0
        scoreList.append('Kίνηση '+str(key)+'.')
        for i in score[key]:
            if l==0:
                scoreList.append('          Το σκορ σου:     '+ str(i))
                l+=1
            else:
                scoreList.append('          To σκορ του H/Y: '+ str(i))
        scoreList.append('--------------------------------------------------------')
    scoreList.append('\n\n\n')
    file_Name = "score.pkl"
    with open(file_Name,'ab') as f:
        pickle.dump(scoreList,f)


def playMyRound(sac, g, hand, wordDict, n):
    wordPoints = 0
    flag = 0
    size = 0
    print('Στο σακουλάκι: '+ str(sac.letters_in_sak)+' γράμματα - Παίζεις:')
    print("Διαθέσιμα Γράμματα:",end=" ")
    sac.displayLetters(hand)
    newWord = input("Λέξη: ")
    while True:
        if newWord == 'q':
            flag = 1
            print("GAME OVER! ")
            break
            
        if newWord == 'p':
            sac.putBackLetters(hand)
            hand.clear()
            size = sac.numOfLetters
            print('To Σκορ Σου: ' + str(g.mytotalpoints)+ ' points')
            input('Enter για συνέχεια')
            print('---------------------------------------------------------')
            break
        elif g.isValidWord(newWord, hand, wordDict) == True:
            sac.letters_in_sak -= len(newWord)
            size = len(newWord)
            hand = sac.findNotUsedLetters(hand, newWord)
            wordPoints = wordDict[newWord]
            g.mytotalpoints += wordPoints
            print('Αποδεκτή Λέξη' +' - '+ 'Βαθμοί: ' + str(wordPoints) +' - '+ 'Σκορ: ' + str(g.mytotalpoints)+ ' points')
            input('Enter για συνέχεια')
            print('---------------------------------------------------------')
            break
        else:
            flag2 = 0
            newHand = dict(hand)
            for i in newWord:
                if newHand.get(i,0) >= 1:
                    newHand[i] -= 1
                else:
                    flag2=1
                    print("H Λέξη Περιέχει Γράμματα που Δεν Διαθέτεις! Παρακαλώ Προσπάθησε Ξανά.")
                    break
            if flag2==0:
                print("Μη Αποδεκτή Λέξη! Παρακαλώ Προσπάθησε Ξανά.")
            print("Διαθέσιμα Γράμματα:",end=" ")
            sac.displayLetters(hand)
            newWord = input("Λέξη: ")
    return flag, size
            

def playCompRound(sac, alg, g, hand, wordDict, n):       
    flag = 0
    size = 0
    print('Στο σακουλάκι: '+  str(sac.letters_in_sak)+' γράμματα - Παίζει o H/Y:')
    print("Γράμματα Η/Υ:",end=' ')
    sac.displayLetters(hand)
    if alg.algorithm == 1:
        word = alg.minLetters(hand, wordDict, n)
    elif alg.algorithm == 2:
        word = alg.maxLetters(hand, wordDict, n)
    else:
        word = alg.smartLetters(hand, wordDict, n)
        
    if word != None:
        sac.letters_in_sak -= len(word)
        size = len(word)
        hand = sac.findNotUsedLetters(hand, word)
        score = wordDict[word]
        g.comptotalpoints += score
        print('Λέξη Η/Υ: ' + word +', '+ 'Βαθμοί: ' + str(score) +' - '+ 'Σκορ Η/Υ: ' + str(g.comptotalpoints) + ' points')
        input('Enter για συνέχεια')
        print('---------------------------------------------------------')
    else:
        flag = 1
        print("Δεν Υπάρχει Καμία Λεξη στο Λεξικό με τα Διαθέσιμα Γράμματα του Η/Υ!")
        print("GAME OVER! ")
    return flag, size



def playGame(sac,alg, g, wordDict):
    score = dict()
    while True:
        flag = 0
        print('****SCRABBLE****')
        print('----------------')
        print('1:  Σκορ')
        print('2:  Ρυθμίσεις')
        print('3:  Παιχνίδι')
        print('q:  Έξοδος')
        print('----------------')
        userInput = input("Πληκτρολόγησε την επιλογή σου: ")
        if userInput == '1':
            print('\n--------------------')
            print('*ΙΣΤΟΡΙΚΟ ΠΑΙΧΝΙΔΙΩΝ*')
            print('--------------------\n')
            scoreList = []
            file_Name = "score.pkl"
            with open(file_Name,'rb') as f:
                while True:
                    try:
                        scoreList=pickle.load(f)
                        for line in scoreList:
                            print(line)
                    except EOFError:
                        break
        elif userInput == '2':
            print('-----------')
            print('*ΡΥΘΜΙΣΕΙΣ*')
            print('-----------')
            while True:
                print('1: ΜΙΝ Letters')
                print('2: ΜΑΧ Letters')
                print('3: SMART')
                print('--------------------')
                print('Τρέχον Αλγόριθμος: '+ str(alg.algorithm))
                print('--------------------')
                userInput2 = input("Επίλεξε τον αλγοριθμο παιχνιδιού του Η/Υ: ")
                if userInput2 == '1':
                    alg.algorithm = 1
                    print('Eπέλεξες τον αλγόλιθμο 1!')
                    print('---------------------------------------------------------')
                    break
                elif userInput2 == '2':
                    alg.algorithm = 2
                    print('Eπέλεξες τον αλγόλιθμο 2!')
                    print('---------------------------------------------------------')
                    break
                elif userInput2 == '3':
                    alg.algorithm = 3
                    print('Eπέλεξες τον αλγόλιθμο 3!')
                    print('---------------------------------------------------------')
                    break
                else:
                    print('Αδύνατη επιλογή! Δυνατές επιλογές: 1,2,3. Προσπάθησε ξανά!')
        elif userInput == '3':
            print('----------')
            print('*ΠΑΙΧΝΙΔΙ*')
            print('----------')
            a=0
            count=0
            sac = SakClass()
            g = Game()
            myAvailableLetters = {}
            compAvailableLetters = {}
            n1 = sac.numOfLetters
            n2 = sac.numOfLetters
            score = dict()
            sac.letters_in_sak -= 2*sac.numOfLetters
            myAvailableLetters = sac.removeRandomLetters(myAvailableLetters, n1)
            while flag == 0:
                if a % 2 == 0:
                    if not myAvailableLetters:
                        print('Στο σακουλάκι : '+ str(sac.letters_in_sak)+' γράμματα')
                        print('Δεν υπάρχουν αρκετα γράμματά στο σακουλάκι')
                        flag = 1
                    else:    
                        flag, n1 = playMyRound(sac, g, myAvailableLetters, wordDict, sac.numOfLetters)
                        if flag ==0:
                            myAvailableLetters = sac.removeRandomLetters(myAvailableLetters, n1)
                            print("Διαθέσιμα Γράμματα:",end=" ")
                            sac.displayLetters(myAvailableLetters)
                            print('---------------------------------------------------------')
                        a +=1
                else:
                    compAvailableLetters = sac.removeRandomLetters(compAvailableLetters, n2)
                    if not compAvailableLetters :
                        print('Στο σακουλάκι : '+ str(sac.letters_in_sak)+' γράμματα')
                        print('Δεν υπάρχουν αρκετα γράμματά στο σακουλάκι')
                        flag = 1
                    else:
                        flag, n2 =playCompRound(sac, alg, g, compAvailableLetters, wordDict, sac.numOfLetters)
                        a +=1
                count+=1
                score[count] = []
                score[count].append(g.mytotalpoints)
                score[count].append(g.comptotalpoints)
        elif userInput == 'q':
            print('Βye bye...')
            break
        else:
            print('Αδύνατη επιλογή! Δυνατές επιλογές: 1,2,3,q. Προσπάθησε ξανά!')
        if flag==1:
            winner = g.results()
            saveInFile(g,winner, score)
        print('-Επιστροφή στο κύριο Μενού-')
        print('---------------------------------------------------------')
        


if __name__ == '__main__':
    file_Name = "greek7.pkl"
    with open(file_Name,'rb') as f:
        wordDict = pickle.load(f)
    sac = SakClass()
    g = Game()
    alg = Algorithm()
    playGame(sac,alg, g, wordDict)
