import requests
import random


words = []
word_dict = [[],[],[]] 

def fillWordDict():
    word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
    response = requests.get(word_site)
    words = response.content.splitlines()
    random.shuffle(words);
    for word in words:
        len_word = len(word)
        if (len_word > 3 and len_word < 14):
            if (len_word <= 6):                
                word_dict[0].append(word)
            elif (len_word <= 10):                
                word_dict[1].append(word)
            elif (len_word > 10):                
                word_dict[2].append(word)

    return word_dict


def chooseAndPrintWord(d):
    index = random.randint(1,int(len(word_dict[d])))
    word_to_scramble = word_dict[d][index].lower()

    l = list(word_to_scramble)
    random.shuffle(l);
    scrambled_word = ''.join(l)
    return scrambled_word,word_to_scramble 

def startGame():
    round_num = 1
    print " "
    difficulty = 0
    while True:
        level  = raw_input("Ready to play Unscrambler? What level? [ 1 (easy), 2 (medium), or 3 (hard) ]   ")
        if int(level) < 4 and int(level > 0):
            difficulty = int(level) - 1
            break
        else:
            print "Please choose a number between 1 and 3, with 3 being the most difficult."

    print "Let's begin!"
    print "Downloading words..."
    word_dict = fillWordDict()
    word_data = chooseAndPrintWord(difficulty)
    print "Your word is:   " + word_data[0]
    answer = word_data[1]
    attempt = 0
    while (True):
        user_input = raw_input("Answer:   ")
        attempt += 1
        if (user_input == answer):
            print "Correct!!"
            break
        elif (user_input == "Q"):
            print "Quitting..."
            break
        elif (attempt > 3):
            print "Try again! or type Q to quit"
        else:
            print "Try again!"
    
    
    # print " ".join(guess_letters) #word_data[0]
    # while (round_num < 7 and not isGameOver()): 
    #     round_data = runTheRound(word_data[1])
        
    #     if round_data[1] == False:
    #         print "Wrong! Try again. "
    #         round_num+=1

    #     print renderHangman(round_num)
    #     print " ".join(guess_letters)#round_data[0]
    #     print "Wrong Letters:    " + " ".join(wrong_letters)
    #     print "                                "
    #     print "--------------------------------"
    #     print "                                "
    
    # if (isGameOver()):
    #     print "GAME OVER, YOU WIN!!!!"
    # elif (round_num >= 7):
    #     print "GAME OVER, YOU LOSE!!!"

startGame()