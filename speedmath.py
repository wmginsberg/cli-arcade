import time
import random

def start_game():
	difficulty = 0
	maximum = 9
	while True:
		level  = raw_input("Ready to play Speed Math? What level? [ 1 (easy), 2 (medium), or 3 (hard) ]   ")
		if int(level) < 4 and int(level > 0):
			difficulty = int(level)
			break
		else:
			print "Please choose a number between 1 and 3, with 3 being the most difficult."
	maximum = get_maximum(difficulty)
	ready = raw_input("Press enter to begin.   ")
	score = 0
	start = time.time()
	print 'START'

	operands = ['+','-','*']

	for i in range(10):
		a = random.randint(0,maximum)
		b = random.randint(0,maximum)
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
	#print 'Total = ' + str(int((end - start))*score*difficulty)


def get_maximum(diff):
	if (diff == 1):
		return 9
	elif (diff == 2):
		return 20
	else:
		return 50


start_game()