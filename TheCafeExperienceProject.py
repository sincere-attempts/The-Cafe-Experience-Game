# This is a game that simulates ordering your drink at a cafe
# Next add: looking around the room to see if any tables are available
#Table of store inventory and potential for missing ingredients
#Simplify logic tree down to abstracts
#Milk alternatives
# Money feature where if you run out of money you have to work at the cafe to pay off your drink
# Program an ingredients list that can be requested for each drink
#Menu

import time
import random

menu = ['latte', 'tea', 'coffee']


def harmoniousInterlude(): #inserts a 2 second pause and a blank line, for improved pacing of the script
    time.sleep(2)
    print()
    
def displayIntro(): #Welcomes the player to the game and sets up their character name, allows them to choose to start game or exit game
    print('Welcome to The Cafe Experience.')
    harmoniousInterlude()
    print('Now, without leaving your home, you can experience the joy of The Cafe!')
    harmoniousInterlude()
    print('Please choose your character name')
    global CharacterName
    CharacterName = input()
    harmoniousInterlude()
    print('That\'s right, ' + CharacterName + '. I remember now.')
    harmoniousInterlude()
    print('Are you ready to enter The Cafe?')
    choice = input()
    if (choice == 'no'):
            ExitGame()
    else:
            harmoniousInterlude()
            print('You enter The Cafe.')
            harmoniousInterlude()
            print('Remember, you can leave The Cafe at any time by saying, \'I want to leave The Cafe.\'')
            time.sleep(2)
            print('...')
            time.sleep(2)
            print('At least, in theory.')
            inventory = []
            time.sleep(3)
            
            enterCafe()

def enterCafe(): #Dialogue where barista welcomes the player by their chosen name as they walk in
    harmoniousInterlude()
    print()
    print('BARISTA: "Hiii, welcome in!"')
    harmoniousInterlude()
    print('"Oh! ' + CharacterName + '! I didn\'t recognize you!"')
    time.sleep(2)

    approachCounter()

def approachCounter(): #Allows player to order their "usual" or see the menu for more options (which calls the orderingDrink function)
    global current_drink
    print()
    print('"What would you like to order? Your usual? Or do you need to see the menu?"')
    choice = input()
    if (choice == 'usual'):
        time.sleep(2)
        print('Oh no! I forgot your usual, what is it?')
        usual = input()
        time.sleep(2)
        print('Thats right! Your usual is a ' + usual + '!')
        current_drink = usual # check on this
        time.sleep(4)
        makeDrink()
    if (choice == 'menu'):
        readMenu()
        orderingDrink()
    else:
        print('I\'m sorry, I don\'t understand.')
        approachCounter()

def orderingDrink(): #Takes the player's drink order input and confirms what they want to order, allowing them to change their mind or calling the makeDrink function if they're ready
    global current_drink
    done = False
    harmoniousInterlude()
    print('So what looks good?')
    current_drink = input()
    harmoniousInterlude()
    print('"Great, you want to order a "' + current_drink + '"?"')
    while (done == False):
        if input() == 'yes':
            print('You have ordered a "' + current_drink + '".')
            done = True
            makeDrink()
        else:
            orderingDrink()
          

def makeDrink():
    harmoniousInterlude()
    print('BARISTA: "One "' + current_drink + '" coming right up!"')
    if (current_drink == 'coffee'):
        harmoniousInterlude()
        print('"Let me just grab that for you real fast!"')
        time.sleep(20)
        print('"Here you go!"')
        ExitGame()
    if (current_drink == 'tea'):
        harmoniousInterlude()
        print('It\'ll just take about 4 minutes to steep.')
        time.sleep(240)
        print()
        print('All done! Here you go, have a great day,' + CharacterName + '.')
        ExitGame()
    if (current_drink == 'latte'):
        harmoniousInterlude()
        print('"You just have a seat, I\'ll call your name when it\'s done."')
        harmoniousInterlude()
        print('This will take a normal amount of time.')
        time.sleep(180)
        print()
        print('"Hey, ' + CharacterName + ', your drink is ready!"')
        ExitGame()
    else:
        harmoniousInterlude()
        print('"I\'ve never made a "' + current_drink + '" before, but I\'ll do my best!"')
        harmoniousInterlude()
        print('"Just have a seat and I\'ll call your name when it\'s ready!"')
        time.sleep(60)
        print()
        print('"Hey, ' + CharacterName+ ', your "' + current_drink + '" is ready!"')
        time.sleep(2)
        ExitGame()
        
def readMenu(): #Prints a menu of all drinks available
    print('      ~~~~MENU~~~~')
    print(menu)

##def updateMenu(): #Adds new drinks to the menu
     menu = (menu.append(input))
     return menu

def ExitGame():
    harmoniousInterlude()
    print('Do you want to leave The Cafe?')
    choice = input()
    if (choice == 'I want to leave The Cafe.') or (choice == 'yes'):
        quit()
    if (choice == 'I want to leave the cafe.') or (choice == 'I want to leave the cafe'):
        print('You must state these words exactly: I want to leave The Cafe.')
        ExitGame()
    else:
        anotherRound()

def anotherRound():
    print('Do you want another drink?')
    if (input() == 'yes'):
        approachCounter()
    else:
        ExitGame()

playAgain = 'yes'
CharacterName = 'Bob'
while (playAgain == 'yes'):
    displayIntro()
else:
    ExitGame()    
    
