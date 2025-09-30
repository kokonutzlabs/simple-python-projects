#make this into a while loop later
print("Rock, Paper, scissors")

import random
player = 0
computer = 0

player = int(input('''Choose your hand:
1. Rock
2. Paper
3. Scissors
 
 '''))

computer = random.randint(1,2)

if computer == 1 and player == 3:
  print("rock beats scissor, you lost.")
elif computer == 2 and player == 1:
 print("paper beats rock, you lost.")
elif computer == 1 and player == 1:
  print("its a tie, try again.")
elif computer == 2 and player == 2:
  print("its a tie, try again.")
elif computer == 3 and player == 3:
  print("its a tie, try again.")
else:
  print("Yay, you won!!")
