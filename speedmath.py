import time
import random

def start_game():
	ready = raw_input("Press enter to begin.   ")
	score = 0
	start = time.time()
	print 'START'

	operands = ['+','-','*']

	for i in range(10):
		a = random.randint(0,9)
		b = random.randint(0,9)
		op = operands[random.randint(0,2)]

		if (op == '+'):
			ans = a + b 
			guess = raw_input(str(a) + ' + ' + str(b) + ' = ')
			if guess == str(ans):
				score += 1 
		elif (op == '-'):
			ans = a - b
			guess = raw_input(str(a) + ' - ' + str(b) + ' = ')
			if guess == str(ans):
				score += 1 
		else:
			ans = a * b
			guess = raw_input(str(a) + ' * ' + str(b) + ' = ')
			if guess == str(ans):
				score += 1 

	end = time.time()

	print 'Time = ' + str(int(end - start))
	print 'Score = ' + str(score) + ' / 10'
	print 'Total = ' + str(int((end - start))*score)

start_game()