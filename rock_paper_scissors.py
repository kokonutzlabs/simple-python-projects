#make this into a while loop later
print("Rock, Paper, scissors")

import random
score = 0
computer = random.randint(1,3)

player = int(input('''Choose your hand (1-3):
1. Rock
2. Paper
3. Scissors
4. Quit
 '''))
 

while player in [1,2,3]:
    player = int(input('''Choose your hand (1-3):
1. Rock
2. Paper
3. Scissors
4. Quit
 '''))
 
    if computer == player:
        print("its a tie, try again.")
        
    if player in [1, 2, 3]:
        if computer == 1 and player == 3:
            print(f'rock beats scissor, you lost.')
        elif computer == 2 and player == 1:
            print(f'paper beats rock, you lost.')
        elif computer == 3 and player == 2:
            print(f'Scissors beats paper, you lost.')
        else:
            print("Yay, you won!!")
            score != +1

if player == 4:
  print(f'Your score is: {score} pts, bye bye!')

