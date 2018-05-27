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
numOfTries=int(0) # Counter, number of attempts for programs
outputFileName="MastermindGameHistory.txt" # .txt filename
outputFile=Path("MastermindGameHistory.txt") # .txt file location
# Menu Input
menu_inp=input("Would you like to begin(Yes/No): ")
# Game Section
if (menu_inp=="Yes"): # User selection "Yes"
    while (playingMastermind==1):
        for i in range(0,4): # Generating random number to genRandomList
            genRandomList.insert(i,randrange(1,7,1))
        #print(genRandomList) # Debug tool
        if outputFile.is_file(): # Check if .txt file exists
            myfile=open(outputFileName, 'a') # Open .txt file under Append
        else:
            myfile=open(outputFileName, 'w') # Create .txt file under Write
        myfile.write('*******GAME START*******\n Randomly Generated Number: ')
        for y in range(0,4):
            myfile.write(str(genRandomList[y])) # Writing genRandomList to .txt
        myfile.write("\n")
        # Game Instructions
        print("\nEnter your guess using a 4 digit code (follow the scheme below).\nYou are to guess the randomly generated 4 colour pattern.")
        print("1 - White\n2 - Blue\n3 - Red\n4 - Yellow\n5 - Green\n6 - Purple\n")
        while (numOfTries<8):
            print("Try number: ",numOfTries+1)
            userGuess=str(input("Enter your guess: ")) # User's guess
            if (len(userGuess)<4 or len(userGuess)>4): #userGuess length check
                print("\n",userGuess," is not 4 digits")
            else:
                for h in range(0,4): # userGuess check with range rules
                    userGuessList.insert(h,int(userGuess[h]))
                    if (int(userGuess[h])>=1 and int(userGuess[h])<=6):
                        userGuessRangeCheck+=1
                if (int(userGuess)==0): # '0000' emergency exit
                    numOfTries=10
                elif (genRandomList==userGuessList): # 'Won the game' exit
                    print("\nCongratulations !!!!! You have won the game…")
                    myfile.write('User won the game at try number: ')
                    myfile.write(str(numOfTries+1))
                    numOfTries=11
                else:
                    if (userGuessRangeCheck!=4):
                        print("\nFrom your 4 digit guess of ",userGuess," ,",(4-userGuessRangeCheck)," digit(s) were not within the range of 1-6")
                    else:
                        myfile.write('Try number: ')
                        myfile.write(str(numOfTries+1))
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
                        print("Tries :",numOfTries+1, end="     ")
                        print("Guess :",userGuess, end="     ")
                        print("Clue :", end="")
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
            myfile.write('The user decided to quit after: ')
            myfile.write(str(numOfTries+1))
            myfile.write(' tries.\n*******GAME END********\n')
            myfile.close()
            input("Press 'Enter' to exit...")
            quit()
        else:
            # Replay Input
            print("\nSorry the number to guess was: ",end="")
            for k in range(0,4):
                print(genRandomList[k],end="")
            playingMastermindAnswer=input("\nWould you like to play another game (Yes/No) ?: ")
            if (playingMastermindAnswer=="Yes"): # 'Yes' choice involves resetting Variables
                numOfTries=0
                userGuess=str()
                userGuessList=[]
                userGuessRangeCheck=0
                genRandomList=[]
                print("\n")
            elif (playingMastermindAnswer=="No"): # 'No' choice
                print("Thank-you for playing.\nHope you had fun.\nShutting down the game.\n")
                playingMastermind=0
            else: # 'Invalid input'choice
                print("Sorry that response was not expected.\nShutting down the game.\n")
                playingMastermind=0
            myfile.write('\n*******GAME END********\n')
            myfile.close()
elif (menu_inp=="No"): # User selection "No"
    print("We'll play again soon.")
else: #User selection not within range
    print("That is not an accepted reply.")
input("Press 'Enter' to exit...")
quit()
