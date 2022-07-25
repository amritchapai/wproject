import random
from words import hangman_words
from main2 import difficult, easy
from function import clearConsole

rungame = 0
while rungame == 0:
    clearConsole()
    choice = int(input("""



                                                    ---------ENTER DIFFICULTY---------
                                    1 FOR EASY
                                    2 FOR DIFFICULT
                                    3 EXIT GAME

    """))
    if choice == 1:
        clearConsole()
        easy()
        print("\n")
        play = int(input("""                                    DO YOU WANT TO PLAY AGAIN??
                                     1 YES
                                     2 NO
        
        """))
        if play == 2:
            rungame = 1
            print("             ------------Thanks for playing-------------")
        else:
            rungame = 0

    elif choice == 2:

        clearConsole()
        difficult()
        print("\n")
        play = int(input("""                                    DO YOU WANT TO PLAY AGAIN??
                                     1 YES
                                     2 NO
        
        """))
        if play == 2:
            rungame = 1
            print("             ------------Thanks for playing-------------")
        else:
            rungame = 0
    elif choice == 3:
        clearConsole()
        print("             ------------Thanks for playing-------------")
        rungame = 1
    else:
        clearConsole()
        print("ENTER EITHER 1 OR 2")
