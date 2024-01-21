

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

# Menu items
SYRUP_OPTIONS = 'vanilla caramel lavender mocha'.split()
MILK_OPTIONS = 'whole 2% nonfat soy coconut oat almond'.split()
BASE_OPTIONS = 'latte cappucino cortado coffee tea'.split()

ALL_OPTIONS = [SYRUP_OPTIONS, MILK_OPTIONS, BASE_OPTIONS]


player_syrup = ''
player_base = ''
player_milk = ''
player_usual = 'water'

CharacterName = 'Bob'

# Prints barista face

def beautifulBarista():
    print('''
      _____ 
    /|||||||\ ''', '''
   ||| _  _ || ''', '''
  (o| O-.\-O||\ ''', '''
  //|\   U / |\\ ''', '''
      ||||| ''', '''
     /  0  \ ''','''
''')

# Printing menu
def viewMenu():
    print('~~~~~MENU~~~~~')
    print('Drinks:')
    print(', '.join(BASE_OPTIONS))
    print()
    print('Flavors: ')
    print(', '.join(SYRUP_OPTIONS))
    print()
    print('Milks: ')
    print(', '.join(MILK_OPTIONS))
    print()
    print('Are you ready to order?')
    if input() == 'yes':
         orderingDrink()
    else:
        viewMenu()


def harmoniousInterlude(): #inserts a 2 second pause and a blank line, for improved pacing of the script
    time.sleep(2)
    print()
    
def displayIntro(): #Welcomes the player to the game and sets up their character name, allows them to choose to start game or exit game
    print('''              ~ ----------------------------------------------------- ~
              |                      Welcome to                       | 
              |                  THE CAFE EXPERIENCE                  |
              =========================================================
                                                                        ''')
    harmoniousInterlude()
    print('Now, without leaving your home, you can experience the joy of The Cafe!')
    harmoniousInterlude()
    print('Please choose your character name')
    global CharacterName
    CharacterName = input()
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
    beautifulBarista()
    print('BARISTA: "Hiii, welcome in!"')
    harmoniousInterlude()
    print('"Oh! ' + CharacterName + '! I didn\'t recognize you!"')
    time.sleep(2)

    approachCounter()

def approachCounter(): #Allows player to order their "usual" or see the menu for more options (which calls the orderingDrink function)
    print()
    print('"What would you like to order? Your usual? Or do you need to see the menu?"')
    choice = input()
    if (choice == 'usual'):
        time.sleep(2)
        print('Oh no! I forgot your usual, what is it?')
        usual = input()
        time.sleep(2)
        print('Thats right! Your usual is a ' + usual + '!')
        time.sleep(4)
        makeDrink(usual)
    if (choice == 'menu'):
        viewMenu()
    if (choice == 'surprise me'):
        select_ingredients('SURPRISE ME_OPTIONS')
    else:
        print('I\'m sorry, I don\'t understand.')
        approachCounter()

def orderingDrink(): #Takes the player's drink order input and confirms what they want to order, allowing them to change their mind or calling the makeDrink function if they're ready
    global player_base
    print('So what looks good?')
    player_base = input()
    harmoniousInterlude()
    print('"Great, you want to order a "' + player_base + '"?"')
    if input() == 'yes':
        print('Would you like to customize that?')
        if input() == 'yes':
            customizeDrink()
        else:
            makeDrink(player_base)
    else:
        orderingDrink()
        
def customizeDrink():
     print('Would you like to customize syrup or milk?')
     choice = (input() + '_OPTIONS')
     choice = choice.upper()
     select_ingredients(choice)
            
# Choosing drink options

def select_ingredients(x): ###
    global player_syrup
    global player_milk
    global player_base
    ingredient = ''
    y = True
    while y == True:
        if x != 'SYRUP_OPTIONS' and x != 'MILK_OPTIONS' and x!= 'SURPRISE ME_OPTIONS':
            print('Sorry, please state either "milk," "syrup," or "Surprise me".')
            choice = (input() + '_OPTIONS')
            choice = choice.upper()
            select_ingredients(choice)
        if x == 'SURPRISE ME_OPTIONS':
            randomSyrup = random.randint(0, len(SYRUP_OPTIONS) - 1)
            player_syrup = SYRUP_OPTIONS[randomSyrup]
            randomMilk = random.randint(0, len(MILK_OPTIONS) - 1)
            player_milk = MILK_OPTIONS[randomMilk]
            randomBase = random.randint(0, len(BASE_OPTIONS) - 1)
            player_base = BASE_OPTIONS[randomBase]
            y = False
            x = ''.join([player_syrup, ' ', player_base, ' with ', player_milk, ' milk'])
            makeDrink(x)
        if x == 'SYRUP_OPTIONS':
            ingredient = 'syrup'
        if x == '':
            ingredient = 'milk'
        print('What ' + ingredient + ' would you like?')
        choice = input()
        if ingredient == 'syrup':
            player_syrup = choice
        elif ingredient == 'milk':
            player_milk = choice
        print('Anything else?')
        if input() == 'yes':
            customizeDrink()
        else:
            y = False
            x = ''.join([player_syrup, ' ', player_base, ' with ', player_milk, ' milk'])
            makeDrink(x)
    

def makeDrink(x):
    harmoniousInterlude()
    beautifulBarista()
    print('BARISTA: "One ' + x + ' coming right up!"')
    if (x == 'coffee'):
        harmoniousInterlude()
        print('"Let me just grab that for you real fast!"')
        time.sleep(20)
        print('"Here you go!"')
        ExitGame()
    if (x == 'tea'):
        harmoniousInterlude()
        print('It\'ll just take about 4 minutes to steep.')
        time.sleep(240)
        print()
        print('All done! Here you go, have a great day,' + CharacterName + '.')
        ExitGame()
    if (x == 'latte'):
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
        print('"I\'ve never made a "' + x + '" before, but I\'ll do my best!"')
        harmoniousInterlude()
        print('I... I haven\'t made a lot of things...')
        harmoniousInterlude()
        print('"Just have a seat and I\'ll call your name when it\'s ready!"')
        time.sleep(60)
        print()
        print('"Hey, ' + CharacterName+ ', your ' + x + ' is ready!"')
        time.sleep(6)
        ExitGame()
        

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
while (playAgain == 'yes'):
    displayIntro()
else:
    ExitGame()    
    
