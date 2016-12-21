import requests
import random


guess_letters = []
wrong_letters = [] 

def renderHangman(index):
    line = [[0 for i in range(10)] for j in range(10)]

    line[1][1] = "  ___________ "
    line[2][1] = " |          | "
    line[3][1] = " |          | "
    line[4][1] = " |            "
    line[5][1] = " |            "
    line[6][1] = " |            "
    line[7][1] = " |            "
    line[8][1] = " |___________ "  

    line[1][2] = "  ___________"
    line[2][2] = " |          | "
    line[3][2] = " |          O "
    line[4][2] = " |            "
    line[5][2] = " |            "
    line[6][2] = " |            "
    line[7][2] = " |            "
    line[8][2] = " |___________ "

    line[1][3] = "  ___________"
    line[2][3] = " |          | "
    line[3][3] = " |          O "
    line[4][3] = " |          | "
    line[5][3] = " |          | "
    line[6][3] = " |            "
    line[7][3] = " |            "
    line[8][3] = " |___________ "

    line[1][4] = "  ___________ "
    line[2][4] = " |          | "
    line[3][4] = " |          O "
    line[4][4] = " |         \\| "
    line[5][4] = " |          | "
    line[6][4] = " |            "
    line[7][4] = " |            "
    line[8][4] = " |___________ "

    line[1][5] = "  ___________"
    line[2][5] = " |          | "
    line[3][5] = " |          O "
    line[4][5] = " |         \\|/"
    line[5][5] = " |          | "
    line[6][5] = " |            "
    line[7][5] = " |            "
    line[8][5] = " |___________ "

    line[1][6] = "  ___________ "
    line[2][6] = " |          | "
    line[3][6] = " |          O "
    line[4][6] = " |         \\|/"
    line[5][6] = " |          | "
    line[6][6] = " |         /  "
    line[7][6] = " |            "
    line[8][6] = " |___________ "

    line[1][7] = "  ___________ "
    line[2][7] = " |          | "
    line[3][7] = " |          O "
    line[4][7] = " |         \\|/"
    line[5][7] = " |          | "
    line[6][7] = " |         / \\"
    line[7][7] = " |            "
    line[8][7] = " |___________ "

    hangman_string = ''
    for i in range(1,9):
        hangman_string += (line[i][index])
        hangman_string += '\n'

    return hangman_string


def chooseAndPrintWord(difficulty):
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    words = response.content.splitlines()
    random.shuffle(words);
    i = 0
    word = words[i]
    diff_dict = {1:5,2:7,3:15}
    while (len(word) >= diff_dict[difficulty]):
        i+=1
        word = words[i]
    guess_string = "  "

    for x in range(len(word)):
        guess_string += "_ "
        guess_letters.append("_")
    return guess_string,word.lower()

def runTheRound(word):
    guess = raw_input("Guess a letter   ").lower();
    if isValidGuess(guess):
        guess_string = " "
        correct = False
        # If it's in the word
        if (isLetterInWord(guess,word)):
            # Go through the word
            for i in range(len(word)):
                # Edit the index for that letter
                if (guess == word[i]):
                    guess_letters[i] = guess
                    guess_string += (guess + " ")

            return guess_string, True
        # If it's not in the word
        else:
            wrong_letters.append(guess)
            return guess_string, False
        


def isLetterInWord(letter,word):
    for x in range(len(word)):
        if letter == word[x]:
            return True
    return False


def isValidGuess(guess):
    if (len(guess) > 1):
        print "Invalid input. Guess should be one letter."
        return False
    elif (guess not in "abcdefghijklmnopqrstuvwxyz"):
        print "Invalid input. Guess must be a letter" 
        return False 
    return True

def isGameOver():
    for letter in guess_letters:
        if letter == "_":
            return False
    return True

def startGame():
    round_num = 1
    print " "
    difficulty = 0
    while True:
        level  = raw_input("Ready to play Hangman? What level? [ 1 (easy), 2 (medium), or 3 (hard) ]   ")
        if int(level) < 4 and int(level > 0):
            difficulty = int(level)
            break
        else:
            print "Please choose a number between 1 and 3, with 3 being the most difficult."

    print "Let's begin!"
    print renderHangman(round_num)
    word_data = chooseAndPrintWord(difficulty)

    
    print " ".join(guess_letters) #word_data[0]
    while (round_num < 7 and not isGameOver()): 
        round_data = runTheRound(word_data[1])
        
        if round_data[1] == False:
            print "Wrong! Try again. "
            round_num+=1

        print renderHangman(round_num)
        print " ".join(guess_letters)#round_data[0]
        print "Wrong Letters:    " + " ".join(wrong_letters)
        print "                                "
        print "--------------------------------"
        print "                                "
    
    if (isGameOver()):
        print "GAME OVER, YOU WIN!!!!"
    elif (round_num >= 7):
        print "GAME OVER, YOU LOSE!!!"

startGame()