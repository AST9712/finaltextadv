import padlock
gameStageNumber = 0 #This is the stage

def dead():
    print("\nYou are DEAD! Try again...")
    quit()

def getStage():
    global gameStageNumber
    return gameStageNumber
    
def getInput(inputChar):
    global gameStageNumber
    gameStageNumber += 1
    if inputChar == "a":

        answers(inputChar)
        
    elif inputChar == "b":
        
        answers(inputChar)
        
    else:
        print("Fail")
    
def answers(x):
    if getStage() == 1 and x == "a":
        print("You smash your arms downwards shattering the rusty shackles!\n")
    elif getStage() == 1 and x == "b":
        print("You scream for help, unfortunatly the guardian skeleton runs over from\nthe darkness and caves your skull in :(")
        dead()
    elif getStage() == 2 and x == "a":
        print("You run head on into the skeleton guardian.\nHe stabs you with a huge spiked bone shard :(")
        dead()
    elif getStage() == 2 and x == "b":
        print("You get on your knees and dart behind the crate\nTrying to make as little noise as possible")
    elif getStage() == 3 and x == "a":
        print("You run head on into the skeleton guardian.\nYou thrust the knife into his ribs\nUnfortunatly the knife shatters on impact and he caves your skull in :(")
        dead()
    elif getStage() == 3 and x == "b":
        print("The knife flies through the air, you hear a crack\nWhatever was standing there sounds injured!")
    elif getStage() == 4 and x == "a":
        print("Walking slowly towards the creature, you see its a 7ft skeleton\nThe head has the knife stuck into the skull, the body is lying on the floor")
        print("You find a scroll inside the ribs! It's a code for the door :)")
    elif getStage() == 4 and x == "b":
        print("As you explore behind you, a huge door")
        padlock.kacper()
        if padlock.win == False:
            print("FALSE")
        elif padlock.win == True:
            print("True")

        #next part of game does kacper's game with guessing

        
    questions()
    
def questions():
    if getStage() == 0:
        print("---------------Welcome to Skeleton Crypt--------------------------")
        print("---------------by Ed, Kacper, Alex, Riaz, and Yaseen--------------")
        print("\n")

        print("You open your eyes to see yourself chained up to a mossywall\nThe dark room is lit by a single candle\nWhat do you do?:")
        print("\na) Try to rip the shackles off?")
        print("b) Shout for help?")
        print("Enter a or b")
        
        getInput(input())
    elif getStage() == 1:
        print("--------------------------------------------------------------------------------")
        print("You are free from your bindings but you hear a noise in the darkness\nYou see a decript crate to the left of you.\nWhat do you do?:")
        print("\na) Run into the darkness and try to find out the cause of the noise?")
        print("b) Crawl behind the crate as quickly as you can?")
        print("Enter a or b")
        
        getInput(input())
    elif getStage() == 2:
        print("--------------------------------------------------------------------------------")
        print("As you kneel down behind the crate you look down and see a rusty knife\nYou decide to pick it up.\nWhat do you do?:")
        print("\na) Run striaght into the darkness with knife in hand\n   You hope to suprise the enemy.")
        print("b) Throw the knife as hard as you can\n   Hoping it will strike the enemy from afar.")
        print("Enter a or b")
        
        getInput(input())
    elif getStage() == 3:
        print("--------------------------------------------------------------------------------")
        print("After hearing the crack you think...")
        print("\na) Grab the candle and walk towards the hurt creature\n   But they might not be dead...")
        print("b) Stay hidden by exploring behind you\n   Leaving the creature might be a good idea")
        print("Enter a or b")
        
        getInput(input())

def gameStart():
    questions()


###############################################################################################################################################################################


gameStart()


    

