#digitcode.py
import random
import time

guessesTaken = 0

print('Enter code in 15 tries to avoid lockout from the lock\n')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('\nenter 3 digit access code..')

number = random.randint(100, 999)
print(number)
while guessesTaken < 15:
	print()
	guess = input('characterName:> ')
	guess = int(guess)
	
	guessesTaken = guessesTaken + 1
	
	if guess < number:
		print('\nNo access, code is too low!')
		
	if guess > number:
		print('\nNo access, code is too high!')

	if guess == number:
		break
        
if guess == number:
	guessesTaken = str(guessesTaken)
	print('\nChecking ...')
	time.sleep(1)
	print('\nVerifying ....')
	time.sleep(1)
	print('...')
	time.sleep(1)
	print('\nCode - correct!')
	print('\nWelcome to the "room"\n')
######## Go into room
	
if guess != number:
	number = str(number)
	print('\n....')
	time.sleep(1)
	print('\n....')
	time.sleep(1)
	print('\nPadlock has jammed, the code was: ' + number)
	print()
########### back to start
