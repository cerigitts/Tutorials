# codedex checkpoint project
# update to include Lizard & Spock
# corrected cpu print from You to CPU

import random


player = 0
cpu = 0


print('===================')
print('Rock Paper Scissors')
print('===================')
print('1) ✊')
print('2) ✋')
print('3) ✌️')
print('4) 🦎')
print('5) 🖖')


player = int(input('Pick a number:'))
cpu = random.randint(1,5)


if player == 1:
    print('You chose: ✊')
elif player == 2:
    print('You chose: ✋')
elif player == 3:
    print('You chose: ✌️')
elif player == 4:
    print('You chose: 🦎')
elif player == 5:
    print('You chose: 🖖')
    
if cpu == 1:
    print('CPU chose: ✊')
elif cpu == 2:
    print('CPU chose: ✋')
elif cpu == 3:
    print('CPU chose: ✌️')
elif cpu == 4:
    print('CPU chose: 🦎')
elif cpu == 5:
    print('CPU chose: 🖖')


# player winning conditions
# 1 beats 3 & 4
# 2 beats 1 & 5
# 3 beats 2 & 4
# 4 beats 2 & 5
# 5 beats 1 & 3


if player == cpu:
    print('It\'s a tie!')
elif (player == 1 and cpu == 3 or cpu == 4) or (player == 2 and cpu == 1 or cpu == 5) or (player == 3 and cpu == 2 or cpu == 4) or (player == 4 and cpu == 2 or cpu == 5) or (player == 5 and cpu == 1 or cpu == 3):
    print('The Player Won!')
else:
    print('The CPU Won!')