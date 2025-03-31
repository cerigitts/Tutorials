#codedex checkpoint project

import random

player = 0
cpu = 0

print('===================')
print('Rock Paper Scissors')
print('===================')
print('1) ✊')
print('2) ✋')
print('3) ✌️')

player = int(input('Pick a number:'))
cpu = random.randint(1,3)

print('You chose: ✋')
print('CPU chose: ✊')
if player == cpu:
    print('It\'s a tie!')
elif (player == 1 and cpu == 3) or (player == 2 and cpu == 1) or (player == 3 and cpu == 2):
    print('The Player Won!')
else:
    print('The CPU Won!')