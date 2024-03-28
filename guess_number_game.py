import random

number = random.randint(1,10)
trial = 3

while trial > 0:
	guess = int(input('what is the number: '))
	print()
	trial -= 1
	if guess > number:
		print('Higher Try Again, {} trials left'.format(trial))
		print()
	elif guess < number :
		print('Lower Try again,{} trials left'.format(trial))
		print()
	else:
		print('Cogrants You Guessed the number with only {} trial(s)'.format(3 - trial))
		break
else:
	print('Sorry Mate!, try next time, Number was {}'.format(number))