# Mastermind Game
#
# Import Libraries
from random import randrange
from pathlib import *
# Declaring variables
genRandomList=[] # Random number generation list
playingMastermind=int(1) # Integer, continue playing game
playingMastermindAnswer=str() # String, prompt to replay game
mmCorrectPlace=int(0) # Counter, correct digit correct place guesses
mmCorrectNumber=int(0) # Counter, counting correct digit wrong place guesses
mmWrongNumber=int(0) # Counter, incorrect digit guesses
userGuess=str() # String, initial guess by user
userGuessList=[] # List, convert userGuess for comparison
userGuessRangeCheck=int(0) # Counter, digits within range
numOfTries=int(0) # Counter, number of attempts for program
userTryExit=int(1) # Counter, number of attempts for .txt print
outputFileName="MastermindGameHistory.txt" # .txt filename
outputFile=Path("MastermindGameHistory.txt") # .txt file location
# Menu Input
menu_inp=input("Would you like to begin(Yes/No): ")
# Game Section
if (menu_inp=="Yes"): # User selection "Yes"
    while (playingMastermind==1):
        for i in range(0,4):
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
        print("Enter your guess using a 4 digit code (follow the scheme below).\nYou are to guess the randomly generated 4 colour pattern.")
        print("1 - White\n2 - Blue\n3 - Red\n4 - Yellow\n5 - Green\n6 - Purple")
        while (numOfTries<8):
            print("Try number: ",numOfTries+1)
            userGuess=str(input("Enter your guess: "))
            if (len(userGuess)<4 or len(userGuess)>4):
                print(userGuess," is not 4 digits")
            else:
                for h in range(0,4): # Check user input complying with range rules
                    userGuessList.insert(h,int(userGuess[h]))
                    if (int(userGuess[h])>=1 and int(userGuess[h])<=6):
                        userGuessRangeCheck+=1
                if (int(userGuess)==0):
                    userTryExit=int(numOfTries+1)
                    numOfTries=10
                elif (genRandomList==userGuessList):
                    print("Congratulations !!!!! You have won the game…")
                    userTryExit=int(numOfTries+1)
                    myfile.write('User won the game at try number: ')
                    myfile.write(str(userTryExit))
                    numOfTries=11
                else:
                    if (userGuessRangeCheck!=4):
                        print("From your 4 digit guess of ",userGuess," ,",(4-userGuessRangeCheck)," digit(s) were not within the range of 1-6")
                    else:
                        userTryExit=int(numOfTries+1)
                        myfile.write('For try number: ')
                        myfile.write(str(userTryExit))
                        myfile.write(' the user guessed: ')
                        myfile.write(userGuess)
                        myfile.write('  ')
                        for j in range(0,4): # Mastermind Game Check
                            if (userGuessList[j]==genRandomList[j]):
                                mmCorrectPlace+=1
                            elif (userGuessList[j] in genRandomList):
                                mmCorrectNumber+=1
                            else:
                                mmWrongNumber+=1
                        print("Tries :",userTryExit, end="     ")
                        print("Guess :",userGuess)
                        for o in range(0,mmCorrectPlace):
                            print("1", end="")
                            myfile.write('1')
                        for p in range(0,mmCorrectNumber):
                            print("0", end="")
                            myfile.write('0')
                        for k in range(0,mmWrongNumber):
                            print("-", end="")
                            myfile.write('-')
                        print("\n")
                        myfile.write('\n')
                        numOfTries+=1
                    mmCorrectPlace=int(0)
                    mmCorrectNumber=int(0)
                    mmWrongNumber=int(0)
                    userGuess=str()
                    userGuessList=[]
                    userGuessRangeCheck=int(0)
        if (numOfTries==10):
            userTryExit-=1
            myfile.write('The user decided to quit after: ')
            myfile.write(str(userTryExit))
            myfile.write(' tries.\n*******GAME END********\n')
            myfile.close()
            input("Press 'Enter' to exit...")
            quit()
        else:
            playingMastermindAnswer=input("Do you want to play another game (Yes/No) ?: ")
            if (playingMastermindAnswer=="Yes"):
                numOfTries=0
                userGuess=str()
                userGuessList=[]
                userGuessRangeCheck=0
                genRandomList=[]
                playingMastermind=1
            elif (playingMastermindAnswer=="No"):
                print("Thank-you for playing.\nHope you had fun.\nShutting down the game.")
                playingMastermind=0
            else:
                print("Sorry that response was not expected.\nShutting down the game.")
                playingMastermind=0
            myfile.write('\n*******GAME END********\n')
            myfile.close()
elif (menu_inp=="No"): # User selection "No"
    print("We'll play again soon.")
else: #User selection not within range
    print("That is not an accepted reply.")
input("Press 'Enter' to exit...")
quit()
