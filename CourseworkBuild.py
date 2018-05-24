# Mastermind Game
#
# Lib Import
from random import randrange
from pathlib import *
# Declaring variables
genRandomList=[]
playingMastermind=int(1)
playingMastermindAnswer=str()
mmCorrectPlace=int(0)
mmCorrectNumber=int(0)
mmWrongNumber=int(0)
userGuess=str()
userGuessList=[]
userGuessRangeCheck=int(0)
numOfTries=int(0)
outputFileName="MastermindGameHistory.txt"
outputFile=Path("MastermindGameHistory.txt")
#
menu_inp=input("Would you like to begin(Yes/No): ")
#
if (menu_inp=="Yes"):
    while (playingMastermind==1):
        for i in range(0,4): #Generate Random 4 Digit number with each digit having a range of 1-6
            genRandomList.insert(i,randrange(1,7,1))
        print(genRandomList)
        if outputFile.is_file():
            myfile=open(outputFileName, 'a')
        else:
            myfile=open(outputFileName, 'w')
        myfile.write('*******GAME START*******\n Randomly Generated Number: ')
        for y in range(0,4):
            myfile.write(str(genRandomList[y]))
        myfile.write("\n")
        print("Enter your guess using a 4 digit code (follow the scheme below).")
        print(" 1 - White\n 2 - Blue\n 3 - Red\n 4 - Yellow\n 5 - Green\n 6 - Purple")
        while (numOfTries<8):
            print("Try number: ",numOfTries+1)
            userGuess=str(input("Enter your guess: "))
            userGuessExit=int(userGuess)
            if (len(userGuess)<4 or len(userGuess)>4):
                print(userGuess," is not 4 digits")
            else:
                for h in range(0,4): # Check user input complying with range rules
                    userGuessList.insert(h,int(userGuess[h]))
                    if (int(userGuess[h])>=1 and int(userGuess[h])<=6):
                        userGuessRangeCheck+=1
                if (int(userGuess)==0):
                    numOfTries=10
                elif (genRandomList==userGuessList):
                    numOfTries=11
                else:
                    if (userGuessRangeCheck!=4):
                        print("From your 4 digit guess of ",userGuess," ,",(4-userGuessRangeCheck)," digit(s) were not within the range of 1-6")
                    else:
                        for j in range(0,4): # Mastermind Game Check
                            if (userGuessList[j]==genRandomList[j]):
                                mmCorrectPlace+=1
                            elif (userGuessList[j] in genRandomList):
                                mmCorrectNumber+=1
                            else:
                                mmWrongNumber+=1
                        print("Tries :",numOfTries+1, end="     ")
                        print("Guess :",userGuess)
                        for o in range(0,mmCorrectPlace):
                            print("1", end="")
                        for p in range(0,mmCorrectNumber):
                            print("0", end="")
                        for k in range(0,mmWrongNumber):
                            print("-", end="")
                        print("\n")
                        numOfTries+=1
                    mmCorrectPlace=int(0)
                    mmCorrectNumber=int(0)
                    mmWrongNumber=int(0)
                    userGuess=str()
                    userGuessList=[]
                    userGuessRangeCheck=int(0)
        if (numOfTries==10):
            myfile.close()
            input("Press 'Enter' to exit...")
            quit()
        else:
            playingMastermindAnswer=input(" GAME ENDED!\n Would you like to play again (Yes/No): ")
            if (playingMastermindAnswer=="Yes"):
                playingMastermind=1
                numOfTries=0
                userGuess=str()
                userGuessList=[]
                userGuessRangeCheck=0
                genRandomList=[]
                myfile.write(outputEnd,'\n')
                myfile.close()
            elif (playingMastermindAnswer=="No"):
                print(" Thank-you for playing.\n Hope you had fun.\n Shutting down the game.")
                myfile.write('*******GAME END********\n')
                myfile.close()
                playingMastermind=0
            elif (playingMastermind==0):
                print(" Thank-you for playing.\n Hope you had fun.\n Shutting down the game.")
                myfile.write('*******GAME END********\n')
                myfile.close()
            else:
                print("Sorry that response was not expected.\n Shutting down the game.")
                myfile.write('*******GAME END********\n')
                myfile.close()
                playingMastermind=0
elif (menu_inp=="No"):
    print("We'll play again soon.")
input("Press 'Enter' to exit...")
quit()
