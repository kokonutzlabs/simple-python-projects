#clean this l8r
print("Rock, Paper, scissors")

import random
score = 0

print('''
1. Rock
2. Paper
3. Scissors
4. Quit
''')

player = int(input(f'Choose your hand (1-3):'))

while player in [1, 2, 3]:
    computer = random.randint(1,3)
    
    if computer == player:
        print(f'its a tie, try again.')
            
    if player in [1, 2, 3]:
        if computer == 1 and player == 3:
            print(f'rock beats scissor, you lost.')
        elif computer == 2 and player == 1:
            print(f'paper beats rock, you lost.')
        elif computer == 3 and player == 2:
            print(f'Scissors beats paper, you lost.')
        else:
            print("Yay, you won!!")
            score += 1
        
        answer = input(f'Play again?(y/n)')
    if answer == 'y':
        print(int(input(f'Choose your hand (1-3):')))
    else:
        print(f'Your score is: {score} pts, bye bye!')

if player == 4:
    print(f'See ya later!')
else:
    print(f'Incorrect input, try again.')
