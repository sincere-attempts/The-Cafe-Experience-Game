

# This is a game that simulates ordering your drink at a cafe
# Next add: looking around the room to see if any tables are available
#Table of store inventory and potential for missing ingredients
#Simplify logic tree down to abstracts
#Milk alternatives
# Money feature where if you run out of money you have to work at the cafe to pay off your drink
# Program an ingredients list that can be requested for each drink
#Menu

# Add more ascii graphics
# make sure all barista quotes have quote marks
# create a list of phrases barista can say while making your drink and randomly pick one each time
# Tipping feature that increases barista likelihood of giving you a free drink also chance of free drink goes up based on how polite your responses are
# random events or tasks that help you get more money for drinks.
# Goal of game, to get as many drinks as possible.

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
number_drinks = 0
wallet = 20
CharacterName = ''
drink_in_hand = 'empty'
bulletin_cash = 1
couch_cash = 2
bathroom_cash = 5
weasel_cash = 50
morale = ''

# Prints barista face

def beautifulBarista():
    print('''
       ____''','''
      / T  \ ''','''
     | __C__|____ ''',''' 
    /|||||||\ ''', '''
   ||| _  _ || ''', '''
  (o| O-.\-O||\ ''', '''
  //|\   U / |\\ ''', '''
      ||||| ''', '''
     /  0  \ ''','''
''')

def cashMoney():
    print('''
             ''','''
~~~~~~~~~~~~~~~~~~~~~~~~~''','''
| ($)--- .%~*~%. ---($) | ''','''
| |     /%(@>@)%\     | |''','''
| | (O) |%%\-/%%| (O) | |''','''
| |      \_/#\_/      | |  ''','''
| ($) ~~ONE DOLLAR~~ ($)| ''','''
~~~~~~~~~~~~~~~~~~~~~~~~~ ''','''
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
    beautifulBarista()
    print('BARISTA JENNE:')
    print('"Are you ready to order?"')
    if input() == 'yes':
         harmoniousInterlude()
         orderingDrink()
    else:
        print('"All right, just let me know when you\'re ready."')
        baseCommands()


def harmoniousInterlude(): #inserts a 2 second pause and a blank line, for improved pacing of the script
    time.sleep(2)
    print()
    
def displayIntro(): #Welcomes the player to the game and sets up their character name, allows them to choose to start game or exit game
    print('''
        ( ( (                                                                      ( ( (
         ) ) )       ~ ----------------------------------------------------- ~      ) ) )
     _ ---------     |                      Welcome to                       |    --------- _
    \  \       /     |                  THE CAFE EXPERIENCE                  |    \       /  /
      -'-------      =========================================================     ------ '-    
                                                                        ''')
    harmoniousInterlude()
    print('>>> Now, without leaving your home, you can experience the joy of The Cafe!')
    harmoniousInterlude()
    print('>>> The more drinks you buy, the higher your score!')
    harmoniousInterlude()
    print('>>> You start with only $20, but you might find some ways to boost you\'re wallet, if you\'re clever!')
    harmoniousInterlude()
    print('>>> Please choose your character name')
    global CharacterName
    CharacterName = input()
    harmoniousInterlude()
    print('>>> Are you ready to enter The Cafe?')
    choice = input()
    if (choice == 'no'):
            ExitGame()
    else:
            harmoniousInterlude()

            checkInventory()

            harmoniousInterlude()
            print('>>>You enter The Cafe.')
            
            enterCafe()

def checkInventory(): # Displays the character's inventory and stats
    current_amount = str(wallet)
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('                                      ' + CharacterName + ', you have $' + current_amount + ' in your pocket.')
    print('                                  The barista thinks you usually order a ' + str(player_usual) + '.')
    print('                                           You have ordered '+ str(number_drinks) + ' drink(s).')   
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    checkDrink()

def checkDrink():
    if drink_in_hand == 'empty':
        print('                                                   You don\'t have any drinks!')
        harmoniousInterlude()
    else:
        print('Your current drink is a ' + drink_in_hand + '')
        harmoniousInterlude()
        
def enterCafe(): #Dialogue where barista welcomes the player by their chosen name as they walk in
    harmoniousInterlude()
    beautifulBarista()
    print('BARISTA JENNE:')
    print('"Hiii, welcome in!"')
    harmoniousInterlude()
    print('"Oh! ' + CharacterName + '! I almost didn\'t recognize you!"')
    time.sleep(2)

    baseCommands()

def approachCounter(): #Allows player to order their "usual" or see the menu for more options (which calls the orderingDrink function)
    global player_usual
    print()
    print('"So ' + CharacterName + ', you getting your usual? Or do you need to see the menu?"')
    choice = input()
    choice = choice.lower()
    if choice in ('usual', 'my usual', 'the usual', 'getting my usual', 'i\'ll get my usual'):
        if player_usual == 'water':
             print('"Oh dear, you\'re going to have to refresh my memory... What was it?"')
             player_usual = input()
             time.sleep(1)
             print('"That\'s right! Your usual is a ' + player_usual + '!"')
             harmoniousInterlude()
             payDrink(player_usual)
        else:
            print('"Don\'t tell me... you usually get a... ' + player_usual + '!"')
            payDrink(player_usual)
    if choice in ('menu', 'i\'d like to see the menu', 'see menu', 'look menu,' 'look at menu', 'see the menu', 'menu please'):
        viewMenu()   
    if (choice == 'surprise me', 'try something crazy', 'i want to try something crazy', 'how about something crazy', 'something crazy'):
        select_ingredients('SURPRISE ME_OPTIONS')
    else:
        print('"Maybe you should have a look at the menu..."')
        viewMenu()

def orderingDrink(): #Takes the player's drink order input and confirms what they want to order, allowing them to change their mind or calling the makeDrink function if they're ready
    global player_base
    beautifulBarista()
    print('BARISTA JENNE:')
    print('"So what sounds good?"')
    player_base = input()
    harmoniousInterlude()
    print('"Let me see... you said a "' + player_base + '"?"')
    choice = choice.lower()
    if choice in ('yes', 'yep', 'ye', 'y', 'yeah', 'yes please'):
        print('"Would you like to customize that?"')
        if choice in('yes', 'yep', 'ye', 'y', 'yeah', 'yes please'):
            customizeDrink()
        else:
            payDrink(player_base)
    else:
        print('"Sorry, I can\'t hear you over the sound of the blender. What do you want from the menu?"')
        orderingDrink()
        
def customizeDrink():
     print('"What do you feel like changing up? Do you want to add syrup, or are you thinking of going for an alternative milk?"')
     choice = input()
     choice = choice.lower()
     if choice in ('try something crazy', 'i want to try something crazy', 'surprise me', 'i\'m not sure', 'surprise me please', 'surprise me!', 'what do you recommend?',):
          select_ingredients(SURPRISE_ME_OPTIONS)
     if choice in ('both', 'both please', 'milk and syrup', 'syrup and milk', 'syrup milk', 'add syrup and go for alternative milk'):
          select_ingredients(BOTH_OPTIONS)
     if choice in ('syrup', 'flavor', 'pick a flavor', 'add syrup', 'add flavor', 'add a syrup', 'add a syrup please'):
          select_ingredients(SYRUP_OPTIONS)
     if choice in ('milk', 'go for alternative milk', 'alternative milk', 'change milk', 'pick milk', 'change up milk', 'milks', 'alternative milks'):
          select_ingredients(MILK_OPTIONS)
     else:
          print('"I\'m sorry, I don\'t understand. Syrup or milk? Let\'s start there."')
          customizeDrink()
              
# Choosing drink options

def select_ingredients(x): ###
    global player_syrup
    global player_milk
    global player_base
    ingredient = ''
    if x == 'SURPRISE_ME_OPTIONS':
        randomSyrup = random.randint(0, len(SYRUP_OPTIONS) - 1)
        player_syrup = SYRUP_OPTIONS[randomSyrup]
        randomMilk = random.randint(0, len(MILK_OPTIONS) - 1)
        player_milk = MILK_OPTIONS[randomMilk]
        randomBase = random.randint(0, len(BASE_OPTIONS) - 1)
        player_base = BASE_OPTIONS[randomBase]
        x = ''.join([player_syrup, ' ', player_base, ' with ', player_milk, ' milk'])
        print('"Hmmm... how about a ' + x + '?"')
        choice = input()
        choice = choice.lower()
        if choice in ('okay', 'sure', 'sounds good', 'yes', 'let\'s do it!', 'yeah', 'fine', 'sounds great', 'alright', 'all right'):
            payDrink(x)
        else:
            print('"You\'re being picky today, huh? Why don\'t you take another look at the menu?"')
            viewMenu()
    if x == 'SYRUP_OPTIONS':
        print('"What syrup would you like?"')
        choice = input()
        player_syrup = choice
        print('"Sounds good!"')
        x = ''.join([player_syrup, ' ', player_base, ' with ', player_milk, ' milk'])
        payDrink(x)
    if x == 'MILK_OPTIONS':
        print('"What milk would you like?"')
        choice = input()
        player_milk = choice
        print('"Sounds good!"')
        x = ''.join([player_syrup, ' ', player_base, ' with ', player_milk, ' milk'])
        payDrink(x)
    else:
        print('"What syrup would you like?"')
        choice = input()
        player_syrup = choice
        print('"Sounds good! And what kind of milk did you want?"')
        choice = input()
        player_milk = choice
        print('"Okiedoke!"')
        x = ''.join([player_syrup, ' ', player_base, ' with ', player_milk, ' milk'])
        harmoniousInterlude()
        payDrink(x)

def payDrink(x):
    global wallet
    global morale
    price = str(random.randint(2, 10))
    harmoniousInterlude()
    beautifulBarista()
    print('BARISTA JENNE:')
    print('"Okay, that comes out to $' + price + '."')
    price = int(price)
    if(price > wallet) and (morale == high):
        print('"Uh... you don\'t got enough?"')
        print('"You know what, don\'t worry about it, this one\'s on me."')
    elif(price > wallet) and morale != high:
         print('"Uh... Well this is awkward."')
         harmoniousInterlude()
         print('>>> BARISTA JENNE takes back your drink and pours it down the drain."')
         print('BARISTA JENNE:')
         print('"Nice try bud, I\'ve seen this scam a million times."')
         harmoniousInterlude()
         print('"Come back when you\'ve got some cash."')
         harmoniousInterlude()
         print('>>> You leave the counter. Maybe if you tipped more often BARISTA JENNE would have been nicer.')
         baseCommands()
    else:
        price = int(price)
        wallet = wallet - price
        current_amount = str(wallet)
        print('>>> You now have $' + current_amount + ' left.')
        print('>>> Do you want to tip BARISTA JENNE?')
        choice = input()
        choice = choice.lower()
        if choice in ('yes', 'yeah', 'sure', 'yep', 'of course', 'tip', 'leave tip', 'tip jenne', 'tip barista jenne'):
            wallet = wallet - 1
            morale = 'high'
            print('>>> You left BARISTA JENNE a $1 tip. I\'m sure she\'ll appreciate it.')
        else:
            print('>>> You don\'t leave a tip for BARISTA JENNE. Says a lot about society these days. Or maybe just a lot about you.') 
        makeDrink(x)


def makeDrink(x):
    global number_drinks
    global drink_in_hand
    harmoniousInterlude()
    number_drinks = number_drinks + 1
    drink_in_hand = x
    drink_components = ''.split()
    beautifulBarista()
    print('BARISTA JENNE:')
    print('"One ' + x + ' coming right up!"')
    harmoniousInterlude()
    harmoniousInterlude()
    if drink_in_hand == player_usual:
        print('"Ahhhh, you never get tired of drinking ' + drink_in_hand + 's do you?"')
        drinkReady(x)
    if [item for item in drink_components if item in base_options]:
       print('"I feel like I\'ve made this a million times. Let me know if you ever want to try something crazy!"')
       drinkReady(x)
    else:
        print('"I\'ve never made a "' + x + '" before, but I\'ll do my best!"')
    harmoniousInterlude()
    drinkReady(x)

def drinkReady(x):
    harmoniousInterlude()
    harmoniousInterlude()
    print('"Just have a seat and I\'ll call your name when it\'s ready!"')
    time.sleep(20)
    print()
    print('"Hey, ' + CharacterName+ ', your ' + x + ' is ready!"')
    harmoniousInterlude()
    
    checkInventory()

    baseCommands()

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
        harmoniousInterlude()
        checkInventory()
        baseCommands()

def baseCommands():
    global wallet
    global bulletin_cash
    global weasel_cash
    global bathroom_cash
    global couch_cash
    harmoniousInterlude()
    print('>>> What would you like to do next?')
    selection = input()
    selection = selection.lower()
    if selection in ('look', 'look around', 'look around for ideas'):
         print('You are standing in a small, cozy Cafe. A bulletin board holds local business cards and posters, and there\'s a bathroom down the hall.')
         print('The cafe is fairly busy, but there\'s an open table at the back. Or you could grab a spot on the couch.')
         print('You notice Weasel McGee, the town\'s wealthy mayor, has fallen asleep on a big armchair in the corner.')
         print('You can hear Barista Jenne humming a tune while waiting for customers to approach the counter.')
         baseCommands()
    if selection in ('menu', 'see menu', 'look at menu', 'view menu'):
        viewMenu()
    if selection in ('ready to order', 'okay i\'m ready to order', 'i know what i want', 'i\'m ready'):
        orderingDrink()
    if selection in ('inventory', 'view inventory', 'check inventory', 'how much money do i have?', 'items'):
        checkInventory()
    if selection in ('approach counter', 'go to counter', 'order', 'order another drink', 'order something else', 'order again', 'go counter', 'barista', 'order drink', 'get drink', 'get a drink'):
        print('>>>You approach the counter.')
        approachCounter()
    if selection in ('couch', 'sit on couch', 'sit couch'):
            print('You settle into the couch. It feels like being enveloped in a musty hug.')
            print('Seems like it hasn\'t been cleaned in forever, who knows what\'s hidden between the cushions?')
            baseCommands()
    if selection in ('search couch', 'search cushions', 'look between cushions', 'search between cushions', 'look in couch', 'look couch', 'examine couch'):
        if couch_cash == 2:
            print('You rummage around in the cushions and find nothing but dust bunnies, chewed gum, and coffee stains...')
            print('But wait!')
            cashMoney()
            print('You also find a $2 bill! That\'s pretty special, I bet someone will miss that.')
            checkInventory()
            baseCommands()
        else:
            print('You rummage around in the cushions and find nothing but dust bunnies, chewed gum, and coffee stains.')
            baseCommands()
    if selection in ('table', 'take a seat', 'back table', 'sit table', 'sit', 'sit back table'):
        print('You go to sit at the back table and appear to mind your own business while actually people-watching.')
        baseCommands()
    if selection in ('bulletin board', 'look bulletin board', 'look at bulletin board', 'business cards', 'look business cards'):
        if bulletin_cash == 1:
            print('You see business cards for yoga studios, lawn care, and local artists. But... what\'s this?')
            cashMoney()
            print('>>> You find a $1 bill someone has left on the board, inscribed in sharpie with the words "somebody loves you!"')
            wallet = wallet + 1
            bulletin_cash = 0
            checkInventory()
            baseCommands()
        else:
           print('You see business cards for yoga studios, lawn care, and local artists.')
           print('You remember fondly the time when you found a free $1 bill here.')
           baseCommands()
    if selection in ('weasel', 'weasel mcgee', 'look weasel mcgee', 'look weasel', 'approach weasel', 'approach weasel mcgee'):
           print('Weasel McGee snores loudly beside an empty cup of decaf, pockets bulging with bribes.')
           baseCommands()
    if selection in ('pockets weasel mcgee', 'take bribe', 'take bribes', 'rob weasel', 'rob weasel mcgee', 'pickpocket weasel', 'rob', 'pickpocket weasel mcgee', 'steal', 'pickpocket', 'steal from weasel mcgee', 'steal from weasel', 'pockets', 'search weasel', 'search weasel mcgee'):
        if weasel_cash == 50:
            print('You look around to make sure nobody is watching, and then reach into Weasel McGee\'s pocket...')
            print('...')
            cashMoney()
            print('You pull out a wad of cash!')
            print('Weasel McGee snorts and starts to wake up, and you quickly make your escape.')
            wallet = wallet + 50
            weasel_cash = 0
            checkInventory()
            baseCommands()
        else:
            print('Better not push your luck. Besides, don\'t they probably have security cameras in here?')
            baseCommands()
    if selection in ('say hi', 'hi', 'hello', 'hi!', 'hello!', 'thanks', 'thank you', 'hi jenne'):
        print()
        print('"Please make yourself at home and let me know when you\'re ready to order!"')
        baseCommands()
    if selection in ('bathroom', 'go bathroom', 'go to bathroom', 'go to the bathroom', 'restroom', 'look bathroom', 'poop', 'pee'):
               if bathroom_cash == 5:
                   print('You go to the bathroom, feeling the sudden urge to take a huge dump.')
                   print('As you sit contemplatively on the toilet, a flash of green catches your eye!')
                   harmoniousInterlude()
                   cashMoney()
                   print('You find a $5 bill on the ground!')
                   wallet = wallet + 5
                   bathroom_cash = 0
                   checkInventory()
                   harmoniousInterlude()
                   print('>>>You finish up your business and head back into the cafe.')
                   baseCommands()
               else:
                   print('Headed to the bathroom again... maybe should cut back on the caffeine.')
                   print('>>> You finish up your business and head back into the cafe.')
                   baseCommands()
    if selection in ('help'):
        print('Try typing commands like "look", "look at ___", "order drink", "sip drink", etc.')
        baseCommands()     
    if selection in ('drink','drink drink', 'drink ' + drink_in_hand + '', 'sip drink', 'have drink', 'sip'):
          if drink_in_hand == '':
              print('>>> You don\'t appear to have a drink. Maybe you should go to the counter and order something.')
              baseCommands()
          else:
              print('>>>You take a nice, long sip of your ' + drink_in_hand + ' and enjoy The Cafe Experience.')
              baseCommands()
    else:   
        print('Sorry, I don\'t understand that command. Try looking around for ideas.')
        baseCommands()
            
playAgain = 'yes'
displayIntro()
while (playAgain == 'yes'):
    baseCommands()

    
else:
    ExitGame()    
    
