#Ce programme a pour but de creer des mots similaire a ceux de la langue francaise
#Il va commencer par passer sur une la listes de mot francais et voir quelles lettres se suivent et lesquelles ne se suivent pas pour en déduire la prochaine lettre.
from math import *
from json import *

import os

DICTIONARY_FILE_NAME = "ods5.txt"

letterCouple = []

a = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet = a.split(" ")

def CalculateCouple():
    words = []

    #read the dictionary of all the words
    with open(DICTIONARY_FILE_NAME, encoding="UTF-8") as f:
        [words.append(line.strip()) for line in f.readlines()]
        
        

    _letterCouple = []
    numbers = []

    for z in range(26):
        numbers.append(0)
        lst = []
        for g in range(26):
            lst.append(0)
        _letterCouple.append(lst)

    # a-a.4 = a with a =  40%


    #peupler letterCouple
    for i in range(len(words)):
        for j in range(len(words[i])-1):
                numbers[alphabet.index(words[i][j])] += 1
                _letterCouple[alphabet.index(words[i][j])][alphabet.index(words[i][j+1])] +=1
            
    for x in range(len(_letterCouple)):
        for y in range(len(_letterCouple[0])):
            _letterCouple[x][y] /= numbers[x]

    return _letterCouple


def CalculateFirstletter():
    words = []

    #read the dictionary of all the words
    with open(DICTIONARY_FILE_NAME, encoding="UTF-8") as f:
        [words.append(line.strip()) for line in f.readlines()]
        
        

    startingLetter = []
    numbers = 0

    for z in range(26):
        startingLetter.append(0)


    #peupler startingCouple
    for i in range(len(words)):
        numbers += 1
        # print(startingLetter[alphabet.index(words[i][0])])
        startingLetter[alphabet.index(words[i][0])] +=1
            
    for x in range(len(startingLetter)):
        startingLetter[x] /= numbers

    return startingLetter

def LoadJson(FileName):
    data = []
    with open(FileName + ".json", "r") as f:
        data = load(f)
    return data

def LoadTxt(FileName):
    f = open(FileName+".txt", "r")
    return float(f.read())
        

def ShowCouple(couples):
    for x in range(len(couples)):
        for y in range(len(couples[0])):
            print(str(alphabet[x]) + "<=>" + str(alphabet[y]) +  " = " + str(round(couples[x][y]*100, 6)) + "%")


def ShowStartingLetters(startingLetter):
    r = 0
    for x in range(len(startingLetter)):
        print(str(alphabet[x]) + " = " + str(round(startingLetter[x]*100, 6)) + "%")

def WriteFiles(data, fileName):
    json_data = dumps(data)
    f = open(fileName + ".json", "w")
    f.write(json_data)
    f.close()

def WriteFile(data, fileName):
    f = open(fileName + ".txt", "w")
    f.write(data)
    f.close()

def GetCouples():
    if not os.path.isfile("couples.json"):
        print("File for couples doesn't exist  !")
        print("calculating couples...")
        _letterCouple = CalculateCouple()
        print("Couples calculated")
        print("Do you want to saves couples to json? (increase starting speed of the program) ('yes' or 'no')")
        inp = input()
        if inp.lower() == "y" or inp.lower() == "yes":
            print("Writing couples.json...")
            WriteFiles(_letterCouple, "couples")
            print("Writed !")
    else:
        print("Reading couples.json...")
        _letterCouple = LoadJson("couples")
        print("Finished !")

    return _letterCouple

def GetStartingLetters():
    if not os.path.isfile("startingLetters.json"):
        print("File for starting letters doesn't exist  !")
        print("calculating starting letters...")
        _startingLetters = CalculateFirstletter()
        print("starting letters calculated")
        print("Do you want to saves starting letters to json? (increase starting speed of the program) ('yes' or 'no')")
        inp = input()
        if inp.lower() == "y" or inp.lower() == "yes":
            print("Writing couples.json...")
            WriteFiles(_startingLetters, "startingLetters")
            print("Writed !")

    else:
        print("Reading startingLetters.json...")
        _startingLetters = LoadJson("startingLetters")
        print("Finished !")
    
    return _startingLetters
    
def CalculateWordLen():
    words  = []
    #read the dictionary of all the words
    with open(DICTIONARY_FILE_NAME, encoding="UTF-8") as f:
        [words.append(line.strip()) for line in f.readlines()]
        
        

    size = 0
    wordsLen = 0

    #peupler startingCouple
    for i in range(len(words)):
        size +=1
        wordsLen += len(words[i])
            

    return wordsLen/size
    # return wordsLen


WORDLENNAME = "worldLen"

def GetWordLen():
    if not os.path.isfile(WORDLENNAME+".txt"):
        print("File for length of words doesn't exist  !")
        print("calculating words len average...")
        average = CalculateWordLen()
        print("starting letters calculated")
        print("Do you want to saves average length to json? (increase starting speed of the program) ('yes' or 'no')")
        inp = input()
        if inp.lower() == "y" or inp.lower() == "yes":
            print(f"Writing {WORDLENNAME}.txt...")
            WriteFile(str(average), WORDLENNAME)
            print("Writed !")

    else:
        print(f"Reading {WORDLENNAME}.txt...")
        average = LoadTxt(WORDLENNAME)
        print("Finished !")
    
    return average

def GenerateWord():
    print("generating...")
def main():
    letterCouple = GetCouples()
    startletter = GetStartingLetters()
    wordLen = GetWordLen()


    while True:
        print("")
        print("-type 'sc' to show all couples.")
        print("-type 'ss' to show star letters proba.")
        print("-type 'wl' to show average words len.")
        print("-type 'c' to clear console.")
        print("-type 'q' to stop program.")
        print("-type 'g' to generate word.")

        inp = input()
        if inp.lower() == "sc":
            ShowCouple(letterCouple)
        elif inp.lower() == "q" or inp.lower() == "quit":
            exit()
        elif inp.lower() == "c" or inp.lower() == "clear":
            os.system('cls')
        elif inp.lower() == "ss":
            ShowStartingLetters(startletter)
        elif inp.lower() == "wl":
            print(wordLen)

        elif inp.lower() == "g" or inp.lower() == "generate":
            GenerateWord()

        else:
            print("Incorect syntax !")
        



main()
