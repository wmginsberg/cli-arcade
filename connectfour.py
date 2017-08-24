import random
import unittest

BOARD_HEIGHT = 8
BOARD_WIDTH = 7
BOTTOM_LABELS = ['A','B','C','D','E','F','G']

LAST_MOVE = [0,0]

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

def make_test_board():
	board = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
	board.append(BOTTOM_LABELS)
	return board

def print_board(board):
	for r in range(BOARD_HEIGHT + 1):
		row = '|'
		for c in range(BOARD_WIDTH):
			if (board[r][c] == 0):
				row += '   |'
			elif (board[r][c] == 3):
				row += ' 0 |'
				LAST_MOVE = [r,c]
			elif (board[r][c] == 2):
				row += ' X |'
				LAST_MOVE = [r,c]
			else:
				row += (' ' + BOTTOM_LABELS[c] + ' |')
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
	else:
		if col.upper()=='Q':
			print 'Quitting...'
			return board,False
		else:
			print 'Invalid input, must be A-G'
			turn = not turn
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
	# diagonal positive slope
	for c in range(BOARD_WIDTH):
		for r in range(BOARD_HEIGHT + 1):
			if (turn): # 0 turn 
				if (board[r][c] == 3):
					if (c < BOARD_WIDTH-4 and r > 3):
						if (board[r-1][c+1]==3 and board[r-2][c+2]==3 and board[r-3][c+3]==3):
							print 'PLAYER 0 WINS'
							return True
			else: # X turn 
				if (board[r][c] == 2):
					if (c < BOARD_WIDTH-4 and r > 3):
						if (board[r-1][c+1]==2 and board[r-2][c+2]==2 and board[r-3][c+3]==2):
							print 'PLAYER X WINS'
							return True
	# diagonal negative slope --- DOESNT WORK
	for c in range(BOARD_WIDTH):
		for r in range(BOARD_HEIGHT+1):
			if (turn): # 0 turn 
				#print c,r,board[r][c]
				if (board[r][c] == 3):
					if (c < 4 and r < BOARD_HEIGHT-3):
						if (board[r+1][c+1]==3 and board[r+2][c+2]==3 and board[r+3][c+3]==3):
							print 'PLAYER 0 WINS'
							return True
			else: # X turn 
				if (board[r][c] == 2):
					if (c < 4 and r < BOARD_HEIGHT-3):
						if (board[r+1][c+1]==2 and board[r+2][c+2]==2 and board[r+3][c+3]==2):
							print 'PLAYER X WINS'
							return True

#game_start()


'''

TESTING ZONE!!! 

'''
class TestMethods(unittest.TestCase):

	def test_horizontal_x(self):
		b = make_test_board()
		b[2][3] = 2
		b[2][4] = 2
		b[2][5] = 2
		b[2][6] = 2
		self.assertFalse(check_for_win(b,1))
		self.assertTrue(check_for_win(b,0))

	def test_horizontal_o(self):
		b = make_test_board()
		b[4][0] = 3
		b[4][1] = 3
		b[4][2] = 3
		b[4][3] = 3
		self.assertTrue(check_for_win(b,1))
		self.assertFalse(check_for_win(b,0))

	def test_vertical_x(self):
		b = make_test_board()
		b[2][2] = 2
		b[3][2] = 2
		b[4][2] = 2
		b[5][2] = 2
		self.assertFalse(check_for_win(b,1))
		self.assertTrue(check_for_win(b,0))

	def test_vertical_o(self):
		b = make_test_board()
		b[1][6] = 3
		b[2][6] = 3
		b[3][6] = 3
		b[4][6] = 3
		self.assertTrue(check_for_win(b,1))
		self.assertFalse(check_for_win(b,0))

	def test_positive_diagonal_x(self):
		b = make_test_board()
		b[1][4] = 2
		b[2][3] = 2
		b[3][2] = 2
		b[4][1] = 2
		#print_board(b)
		self.assertFalse(check_for_win(b,1))
		self.assertTrue(check_for_win(b,0))

		b2 = make_test_board()
		b2[1][5] = 2
		b2[2][4] = 2
		b2[3][3] = 2
		b2[4][2] = 2
		#print_board(b2)
		self.assertFalse(check_for_win(b2,1))
		self.assertTrue(check_for_win(b2,0))
		#top row not being read

	def test_negative_diagonal_x(self):
		b = make_test_board()
		b[2][3] = 2
		b[3][4] = 2
		b[4][5] = 2
		b[5][6] = 2
		print_board(b)
		self.assertFalse(check_for_win(b,1))
		self.assertTrue(check_for_win(b,0))

		b2 = make_test_board()
		b2[0][0] = 2
		b2[1][1] = 2
		b2[2][2] = 2
		b2[3][3] = 2
		print_board(b2)
		self.assertFalse(check_for_win(b2,1))
		self.assertTrue(check_for_win(b2,0))
		#top row not being read

		b3 = make_test_board()
		b3[7][6] = 2
		b3[6][5] = 2
		b3[5][4] = 2
		b3[4][3] = 2
		print_board(b3)
		self.assertFalse(check_for_win(b3,1))
		self.assertTrue(check_for_win(b3,0))
		#top row not being read

	def test_positive_diagonal_o(self):
		b = make_test_board()
		b[1][4] = 3
		b[2][3] = 3
		b[3][2] = 3
		b[4][1] = 3
		#print_board(b)
		self.assertFalse(check_for_win(b,0))
		self.assertTrue(check_for_win(b,1))

		b2 = make_test_board()
		b2[1][5] = 3
		b2[2][4] = 3
		b2[3][3] = 3
		b2[4][2] = 3
		#print_board(b2)
		self.assertFalse(check_for_win(b2,0))
		self.assertTrue(check_for_win(b2,1))
		#top row not being read

# Run the test
unittest.main()
