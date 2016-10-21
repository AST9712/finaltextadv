#digitcode.py
import random
import time

def kacper():
        win = False
        guessesTaken = 0
        print('Enter name:\n')
        name = input()
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('....')
        time.sleep(1)
        print('\nenter 3 digit access code...')

        number = random.randint(100, 999)
        print(number)
        while guessesTaken < 15:
                print()
                guess = input(name + " --> ")
                guess = int(guess)
                
                guessesTaken += 1
                
                if guess < number:
                        print("\nINVALID CODE, too low! " + str(15 - guessesTaken) + " tries left")
                        
                        
                if guess > number:
                        print("\nINVALID CODE, too high!" + str(15 - guessesTaken) + " tries left")

                if guess == number:
                        win = True
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


