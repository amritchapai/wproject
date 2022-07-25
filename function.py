from random import randint
from sys import setswitchinterval
import os


def out(word, entered, tries):
    if tries == 0:
        print("""            ---------------------------
                        ------hangman game---------
       
                               _________________                  
                              |                 |   
                              |                 __
                              |               /   \ 
                              |               \ _ /
                              |              \  | /
                              |               \ |/
                              |                 |
                              |                / \ 
                              |               /   \ 



        !!!!!!!!!!!YOU LOOSE, YOU NOOB!!!!!!!!!!
        

        """)
    elif tries == 1:
        print("""            ---------------------------
                        ------hangman game---------
       
                               _________________                  
                              |                 |   
                              |                 __
                              |               /   \ 
                              |               \ _ /
                              |              \  | /
                              |               \ |/
                              |                 |
                              |                / 
                              |               /   
        
    
        
        """)
    elif tries == 2:
        print("""               ---------------------------
                     ------hangman game---------
       
                               _________________                  
                              |                 |   
                              |                 __
                              |               /   \ 
                              |               \ _ /
                              |              \  | /
                              |               \ |/
                              |                 |
                              |                 
                              |                   


        """)
    elif tries == 3:
        print("""            ---------------------------
                        ------hangman game---------
       
                               _________________                  
                              |                 |   
                              |                 __
                              |               /   \ 
                              |               \ _ /
                              |              \  | 
                              |               \ |
                              |                 |
                              |                 
                              |                   


        """)
    elif tries == 4:
        print("""             ---------------------------
                     ------hangman game---------
       
                               _________________                  
                              |                 |   
                              |                 __
                              |               /   \ 
                              |               \ _ /
                              |                 | 
                              |                 |
                              |                 |
                              |                 
                              |                   


        """)
    elif tries == 5:
        print("""           ---------------------------
                    ------hangman game---------
       
                               _________________                  
                              |                 |   
                              |                 __
                              |               /   \ 
                              |               \ _ /
                              |                  
                              |                 
                              |                 
                              |                 
                              |                   


        """)
    else:
        print("""               ---------------------------
                     ------hangman game---------
       
                               _________________                  
                              |                 |   
                              |                 
                              |                   
                              |               
                              |                  
                              |                 
                              |                 
                              |                 
                              |                   


        """)

    length = len(word)
    for i in range(length):
        print(f"____{entered[i]}_____      ", end=' ')


def check(entered, character):
    flag = 0
    for l in entered:
        if character == l:
            flag = 1
    if flag == 1:
        return 1
    else:
        return 0


def end(matched, length):
    for i in range(length):
        if matched[i] == '#':
            return 0
            break
    return 1


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def hint(matched, choose_word, length, entered):
    flag = 0
    if length > 5:
        while flag == 0:
            ran1 = randint(0, length-1)
            ran2 = randint(0, length-1)
            if ran1 == ran2:
                flag = 0
            else:
                flag = 1
        for i in range(length):
            if i == ran1 or i == ran2:
                matched.pop(i)
                matched.insert(i, choose_word[i])
    else:
        ran1 = randint(0, length)
        for i in range(length):
            if i == ran1:
                matched.pop(i)
                matched.insert(i, choose_word[i])
