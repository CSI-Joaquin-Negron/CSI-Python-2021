import random
word_list = ['bucana', 'jacaguas', 'guajataka', 'fajardo', 'loco', 'bayagan', 'nigua', 'pastillo', 'cerrillos', 'daguao']

def get_word(word_list):
    word = random.choice
    return word.upper()

def play(word):
    word_completion = '_' + len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('HANGMAN!')
    print('Theme: Rios de Puerto Rico')
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input('Guess a Letter or word').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already tried that letter.', guess, "!")
            elif guessed not in word:
                print(guess, "isnt in the word").upper
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Nice!',guess, 'Light Work')
                guessed_letters.append(guess)




def display_hangman(tries):
    stages = ["""
                    --------
                    |    |
                    |    O
                    |   /|\\
                    |    |
                    |   / \\ 
                    """, """
                    --------
                    |    |
                    |    O
                    |   /|\\
                    |    |
                    |   /  
                    """,  """
                    --------
                    |    |
                    |    O
                    |   /|\\
                    |    |
                    |    
                    ""","""
                    --------
                    |    |
                    |    O
                    |   /|\\
                    |    
                    |    
                    """,   """
                    --------
                    |    |
                    |    O
                    |    |\\
                    |   
                    |   
                    """, """
                    --------
                    |    |
                    |    O
                    |    |
                    |   
                    |    
                    """, """
                    --------
                    |    |
                    |    O
                    |   
                    |    
                    |    
                    """, """
                    --------
                    |    |
                    |    
                    |   
                    |    
                    |    
                    """, 
    ]