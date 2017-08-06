import random

BOARD_HEIGHT = 8
BOARD_WIDTH = 7
BOTTOM_LABELS = ['A','B','C','D','E','F','G']

# Functions
def game_start():
	board = make_board()
	print_board(board)
	turn = True
	b,cont = user_turn(board, turn)
	while cont:
		print_board(b)
		turn = not turn
		b,cont = user_turn(board, turn)
		end = check_for_win(board, turn)
		if end:
			print_board(b)
			break
	

def make_board():
	board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
	board.append(BOTTOM_LABELS)
	return board

def print_board(board):
	for r in range(BOARD_HEIGHT + 1):
		row = '|'
		for c in range(BOARD_WIDTH):
			#print '*',r,c
			if (board[r][c] == 0):
				row += '   |'
			elif (board[r][c] == 3):
				#print 'board[r][c] ' + str(board[r][c])
				#print str(r) 
				#print str(c)
				row += ' 0 |'
			elif (board[r][c] == 2):
				row += ' X |'
			else:
				row += (' ' + BOTTOM_LABELS[c] + ' |')
		#print board[r]
		print row




def user_turn(board,turn):
	col = raw_input("It's your turn! Which column would you like to play in?\n>>>   ").upper()
	if (isValidCol(col)):
		found = False
		for i in range(len(BOTTOM_LABELS)):
			if ((col == BOTTOM_LABELS[i]) and found==False):
				col = i
				found = True
		for row in range(BOARD_HEIGHT,0,-1):
			if board[row][col] != 0:
				continue
			else:
				if (turn):
					board[row][col] = 3
				else:
					board[row][col] = 2
				return board,True

def isValidCol(col):
	return ((col in BOTTOM_LABELS) and (len(col) == 1))

def check_for_win(board,turn):
	# horizontal
	count = 0
	for r in range(BOARD_HEIGHT + 1):
		for c in range(BOARD_WIDTH):
			if (turn): # 0 turn 
				if (board[r][c] == 3):
					count += 1
				else:
					count = 0
				if (count == 4):
					print 'PLAYER 0 WINS'
					return True
			else: # X turn 
				if (board[r][c] == 2):
					count += 1
				else:
					count = 0
				if (count == 4):
					print 'PLAYER X WINS'
					return True
	# vertical
	count = 0
	for c in range(BOARD_WIDTH):
		for r in range(BOARD_HEIGHT + 1):
			if (turn): # 0 turn 
				if (board[r][c] == 3):
					count += 1
				else:
					count = 0
				if (count == 4):
					print 'PLAYER 0 WINS'
					return True
			else: # X turn 
				if (board[r][c] == 2):
					count += 1
				else:
					count = 0
				if (count == 4):
					print 'PLAYER X WINS'
					return True


def make_deck():
	pass



game_start()

