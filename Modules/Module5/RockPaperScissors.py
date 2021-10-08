import random

print('Welcome to the rock, paper, scissor game.')
rps = ['rock', 'paper', 'scissor']

playerChoice = input('Choose between Rock, Paper, or Scissor: ')

computerChoice = random.choice(rps)
print(f"Computer selected: {computerChoice}")
print(f"Player selected: {playerChoice}")

if(playerChoice == computerChoice):
    print('TIE!')

elif(playerChoice == "rock" and computerChoice == 'scissor'):
    print('rock beats scissor!')

elif(playerChoice == "rock" and computerChoice == 'paper'):
    print('rock loses to paper!')

elif(playerChoice == "paper" and computerChoice == 'scissor'):
    print('paper loses to scissor!')

elif(playerChoice == "paper" and computerChoice == 'rock'):
    print('paper beats rock!')

elif(playerChoice == "scissor" and computerChoice == 'paper'):
    print('scissor beats paper!')

elif(playerChoice == "scissor" and computerChoice == 'rock'):
    print('scissor loses to rock!')

else:
    print('something is not right')