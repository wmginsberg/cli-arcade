# a collection of cli-based games
#### note: you may need to `pip install` a dependency or two to play

## Hangman
### How to play
* Download `hangman.py`
* Locate the file in your directory
* Run `python hangman.py`

### Features
* Words are based off a public dictionary, pulled from a url, you need internet to play
* You have 7 rounds to win
* Difficulty is based on max length of word
* Quit by typing ctrl-c to kill the program
* Full error checking not entirely implemented

## Unscrambler
### How to play
* Download `unscrambler.py`
* Locate the file in your directory
* Run `python unscrambler.py`

### Features
* Words are based off a public dictionary, pulled from a url, you need internet to play
* You have infinite tries, but you have the option to get a hint (first letter) after 5
* Type Q to quit during a round
* Difficulty is based on length of word

## Connect Four
### How to play
* Download `connectfour.py`
* Locate the file in your directory
* Run `python connectfour.py`

### Features
* 2 player game, Player 0 and Player X. Player 0 goes first
* Type the column to place a chip into it
* Victory can be achieved horizontally, vertically, or diagonally
* Hasn't been entirely tested so there are some bugs
* One known bug: if you give invalid input (a letter that's not A-G, or try to add to a full column, it skips your turn)
* Type Q or q to quit during a game

## Speed Math
### How to play
* Download `speedmath.py`
* Locate the file in your directory
* Run `python speedmath.py`

### Features
* Hit enter to begin and choose a level
* Level 1 gives numbers between 0-9, 2 is 0-20, 3 is 0-50
* You will receive 10 math problems incl. -, +, and * 
* Answer as fast as you can and your time and score will be returned

## Blackjack
### How to play
* Download `blackjack.py`
* Locate the file in your directory
* Run `python blackjack.py`

### Features
* Game is played with an infinite shuffled deck
* No double-down or split (yet :P)
* Minimum bet of 10, maximum of 100
* Quit by typing `quit` or ctrl-c to kill the program


