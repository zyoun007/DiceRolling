# first import random numbers
# if 20 sided dice, print statement for both 20 (critical hit) and 1 (criitcal miss)
# make input amount of sides meaningful as well as rolls on dice
# i'm going to use the input function the amount of sides and number of rolls ex
#print the numbers of the roll
# print your roll is on the output

import random

diceSide = int(input('How Many Sides on Your Dice?'))

diceRoll = int(input('How Many Rolls on Your Dice?'))
if diceRoll == 1:
    print('Your roll is:')
else:
    print('Your rolls are:')

if diceSide == 20:
    for rolls in range(diceRoll):x
        twentyDice = random.randrange(20)+1
        print(twentyDice)
        if twentyDice==20:
            print('critical hit')
        if twentyDice==1:
            print('L BOZO')
else:
    for rolls in range(diceRoll):
        randomDice = random.randrange(diceSide)+1
        print(randomDice)

print ('done rolling') 

#thank you to W3Schools so shout out to them. Helped me remember range

#in range means the amount of rolls
#random.randrange() means the amount of sides

#https://github.com/zyoun007/DiceRolling?search=1
