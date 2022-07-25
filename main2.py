import random
from words import hangman_words
from function import out, check, end, clearConsole, hint


def difficult():
    choose_word = random.choice(hangman_words)
    choose_word = choose_word.upper()
    length = len(choose_word)
    entered = []
    matched = []
    tries = 5
    finish = 0
    flag3 = 0
    for i in range(length):
        matched.append("#")
    while(tries >= 0 and finish == 0):
        print(
            f"                        Number of tries remaining is {tries+1}")
        flag = 0
        flag2 = 0
        out(choose_word, matched, tries+1)
        print("\n")
        print("\n")
        if flag3 == 1:
            print("             !!!!!!!!YOU HAVE GUESSED CORRECT!!!!!!!!!!!!")
            print("\n")
        flag3 = 0
        character = input("   Enter  a letter ")
        character = character.upper()
        clearConsole()
        flag = check(entered, character)
        if flag == 1:
            print("\n")
            print("                 !!!You have already entered this letter!!!!!!")
            print("\n")
        else:
            entered.append(character)
            for j in range(length):
                if character == choose_word[j]:
                    matched.pop(j)
                    matched.insert(j, character)
                    flag2 = 1
                    flag3 = 1
            if flag2 == 0:
                tries = tries - 1
        finish = end(matched, length)
    if finish == 1:
        clearConsole()
        print(f"       THE SECRET WORD WAS {choose_word}")
        print("                 !!!!!!YOU WIN CONGRATULATIONS!!!!!!!!")
    if tries == -1:
        out(choose_word, matched, 0)
        print("\n")
        print(f"         THE SECRET WORD WAS {choose_word}, YOU NOOB")
        print("\n")


def easy():
    choose_word = random.choice(hangman_words)
    choose_word = choose_word.upper()
    length = len(choose_word)
    entered = []
    matched = []
    tries = 5
    finish = 0
    flag3 = 0
    for i in range(length):
        matched.append("#")
    hint(matched, choose_word, length, entered)
    while(tries >= 0 and finish == 0):
        print(
            f"                        Number of tries remaining is {tries+1}")
        flag = 0
        flag2 = 0
        out(choose_word, matched, tries+1)
        print("\n")
        if flag3 == 1:
            print("             !!!!!!!!YOU HAVE GUESSED CORRECT!!!!!!!!!!!!")
            print("\n")
        flag3 = 0
        character = input("             Enter  a letter ")
        character = character.upper()
        clearConsole()
        flag = check(entered, character)
        if flag == 1:
            print("         !!You have already entered this letter!!")
        else:
            entered.append(character)
            for j in range(length):
                if character == choose_word[j]:
                    matched.pop(j)
                    matched.insert(j, character)
                    flag2 = 1
                    flag3 = 1
            if flag2 == 0:
                tries = tries - 1
        finish = end(matched, length)
    if finish == 1:
        clearConsole()
        print(f"    THE SECRET WORD WAS {choose_word}")
        print("                     !!!!!!YOU WIN CONGRATULATIONS!!!!!!!!")
    if tries == -1:
        out(choose_word, matched, 0)
        print("\n")
        print("\n")
        print(f"         THE SECRET WORD WAS {choose_word}, YOU NOOB")
        print("\n")
