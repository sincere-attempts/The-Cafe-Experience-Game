# This is a game that simulates ordering your drink at a cafe
# Next add: looking around the room to see if any tables are available
#Table of store inventory and potential for missing ingredients
#Simplify logic tree down to abstracts
#Milk alternatives

    
import time
import random

def displayIntro():
    print('Welcome to The Cafe Experience.')
    print('Now, without leaving your home, you can experience the joy of Cafe!')
    print('Please choose your character name')
    global CharacterName
    CharacterName = input()

    print('That\'s right, ' + CharacterName + ' I remember now.')
    time.sleep(2)
    choice = input('Are you ready to enter The Cafe?')
    if (choice == 'no'):
            print('oh fuck. okay.')
            time.sleep(3) # pauses before responding
            print('i really dont know what to do with that.')
            time.sleep(5)
            print('please just close the program.')
            time.sleep(10)
            print('seriously, im stuck. you need to just close to program.')
            time.sleep(12)
            print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    else:
            print('You enter The Cafe and approach the counter. Remember, you can leave The Cafe at any time by saying, \'I want to leave The Cafe.\'')
            inventory = []
            
            enterCafe()

def enterCafe():
    print('Hiii, welcome in!')
    time.sleep(2)
    print('Oh! ' + CharacterName + ' I didn\'t recognize you!')
    time.sleep(2)

    orderDrink()

def orderDrink():
    global drink
    choice = input('What would you like to order? Your usual? Or do you need to see the menu?')
    if (choice == 'usual'):
        usual = input('Oh no! I forgot your usual, what is it?')
        print('Thats right! Your usual is a ' + usual + '!')
        drink = usual # check on this
        time.sleep(2)

        makeDrink()
        
    if (choice == 'menu'):
        choice = input('coffee - latte - tea')
        if (choice == 'coffee' or 'tea'):
            creamAndSugar()
            # PROBLEM it's asking ppl who order a latte if they want cream and sugar too. Why?
        else:
            drink = choice

def creamAndSugar():
            additive = input('Would you like cream, sugar, or both?')
            if (additive == 'both'):
                    print("Great choice!")

def makeDrink():
    print('One ' + drink + ' coming right up!')
    if (drink == 'coffee'):
        print('Let me just grab that for you real fast!')
        time.sleep(20)
        print('Here you go!')
        ExitGame()
    if (drink == 'tea'):
        print('It\'ll just take about 4 minutes to steep.')
        time.sleep(240)
        print('All done! Here you go, have a great day,' + CharacterName + '.')
        ExitGame()
    if (drink == 'latte'):
        print('You just have a seat, I\'ll call your name when it\'s done.')
        time.sleep(180)
        print('Hey, ' + CharacterName + ', your drink is ready!')
        ExitGame()
    else:
        print('Just have a seat and I\'ll call your name when it\'s ready!')
        time.sleep(60)
        print('Hey, ' + CharacterName+ ', your drink is ready!')
        time.sleep(2)
        ExitGame()
        
def ExitGame():
    choice = input('Do you want to leave The Cafe?')
    if (choice == 'I want to leave The Cafe.') or (choice == 'yes'):
        quit()
    else:
        playAgain
      
playAgain = 'yes'
CharacterName = 'Bob'
while playAgain == 'yes':
    displayIntro()

    print('Do you want to play again?')
    playAgain = input()
else:
    ExitGame()
    
    
