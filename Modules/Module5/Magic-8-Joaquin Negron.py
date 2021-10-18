import random
playerName = input('What is your name?\n')
print(f'Welcome to the Magic Eight Ball {playerName}!')
m8 = ['Yes, definetly', 'It is decidedly so', 'Without a doubt', 'Reply hazy, try again', 'Ask again later', 'Better not tell you now', 'My sources say no.', 'Outlook not so good', 'Very doubtful', 'Now thats comedic!', 'Can i phone a friend?','Check your cars trunk']
playerChoice = input('You may ask your question:\n')
computerChoice = random.choice(m8)
print(f"{playerName} asked: {playerChoice}")
print(f"{computerChoice}")