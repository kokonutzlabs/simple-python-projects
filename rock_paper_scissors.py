print("Rock, Paper, scissors")

import random
player = 0
computer = 0
score = 0

player = int(input('''Choose your hand (1-3):
1. Rock
2. Paper
3. Scissors
4. Quit
 '''))

computer = random.randint(1,3)

if computer == 1 and player == 3:
  print("rock beats scissor, you lost.")
  player = int(input('''Choose your hand (1-3):
1. Rock
2. Paper
3. Scissors
4. Quit
 '''))
elif computer == 2 and player == 1:
  print("paper beats rock, you lost.")
  player = int(input('''Choose your hand (1-3):
1. Rock
2. Paper
3. Scissors
4. Quit
 '''))
elif computer == 1 and player == 1:
  print("its a tie, try again.")
  player = int(input('''Choose your hand (1-3):
1. Rock
2. Paper
3. Scissors
4. Quit
 '''))
elif computer == 2 and player == 2:
  print("its a tie, try again.")
  player = int(input('''Choose your hand (1-3):
1. Rock
2. Paper
3. Scissors
4. Quit
 '''))
elif computer == 3 and player == 3:
  print("its a tie, try again.")
  player = int(input('''Choose your hand (1-3):
1. Rock
2. Paper
3. Scissors
4. Quit
 '''))
else:
  print("Yay, you won!!")
  score != +1
  player = int(input('''Choose your hand (1-3):
1. Rock
2. Paper
3. Scissors
4. Quit
 '''))

if player == 4:
  print(f'Your score is: {score} pts, bye bye!')
