# Mastermind Game
# Lib Import
from random import randrange
# Declaring variables
genRandomList=[]
userGuessList=[]
playingMastermind=1
playingMastermindAnswer=str()
mmCorrectPlace=int(0)
mmCorrectNumber=int(0)
mmWrongNumber=int(0)
userGuess=str()
userGuessRangeCheck=int(0)
numOfTries=int(0)
# Menu Input
menu_inp=input("Would you like to begin(Yes/No): ")
# Show Time
if (menu_inp=="Yes"):
    while (playingMastermind==1):
        for i in range(0,4):
            genRandomList.insert(i,randrange(1,7,1))
        #genRandomTuple=tuple(genRandomList)
        #print("Let the games begin")
        print(genRandomList)
        print("Enter your guess using a 4 digit code (follow the scheme below).")
        print(" 1 - White\n 2 - Blue\n 3 - Red\n 4 - Yellow\n 5 - Green\n 6 - Purple")
        # Insert WHILE LOOP for 8 times
        while (numOfTries<8):
            print("Try number: ",numOfTries+1)
            userGuess=input("Enter your guess: ")
            if (userGuess!="0000")
                # Check user input complying with range rules
                for h in range(0,4):
                    userGuessList.insert(h,int(userGuess[h]))
                    if (int(userGuess[h])>=1 and int(userGuess[h])<=6):
                        userGuessRangeCheck+=1
                #print(userGuessRangeCheck)
                #print(userGuessList)
                if (userGuessRangeCheck!=4):
                    print("From your 4 digit guess,",(4-userGuessRangeCheck)," digit(s) were not within the range of 1-6")
                else:
                    # Mastermind Game Check
                    for j in range(0,4):
                        if (userGuessList[j]==genRandomList[j]):
                            mmCorrectPlace+=1
                        elif (userGuessList[j] in genRandomList):
                            mmCorrectNumber+=1
                        else:
                            mmWrongNumber+=1
                    print(" mmCorrectPlace ",mmCorrectPlace,"\n mmCorrectNumber ",mmCorrectNumber,"\n mmWrongNumber ",mmWrongNumber)
                mmCorrectPlace=int(0)
                mmCorrectNumber=int(0)
                mmWrongNumber=int(0)
                userGuess=str()
                userGuessRangeCheck=int(0)
                numOfTries+=1
        # Loop to play the game
        playingMastermindAnswer=input(" GAME OVER!\n Would you like to play again (Yes/No): ")
        if (playingMastermindAnswer=="Yes"):
            playingMastermind=1
            # Resetting variables
            numOfTries=0
            userGuess=str()
            userGuessList=[]
            userGuessRangeCheck=0
        elif (playingMastermindAnswer=="No"):
            print(" Thank-you for playing.\n Hope you had fun.\n Shutting down the game.")
            playingMastermind=0
        else:
            print("Sorry that response was not expected.\n Shutting down the game.")
            playingMastermind=0
elif (menu_inp=="No"):
    print("We'll play again soon.")
    input("Press 'Enter' to exit...")
    quit()
else:
    print("Sorry that response was not expected.")
input("Press 'Enter' to exit...")
quit()
