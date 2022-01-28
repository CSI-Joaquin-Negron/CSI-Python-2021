import random
word_list = ['bucana', 'jacaguas', 'guajataka', 'fajardo', 'loco', 'bayagan', 'nigua', 'pastillo', 'cerrillos', 'daguao']

def get_word(word_list):
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = '_ ' * len(word)
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
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("you already tried", guess, "!")
            elif guess != word:
                print(guess, 'is not the word')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed  = True
                word_completion = word
        else:
            print('invalid input')
        print(display_hangman(tries))
        print(word_completion)
        print("\n")

    if guessed:
        ('Good hustle, you finished the word.')
    else:
        ("HE DEAD NOW GOOD ONE! The word was" + word + ', try again maybe?')

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
    return stages[tries]
def main():
    word = get_word(word_list)
    play(word)
    while input('again Y/N').upper() == "Y":
        word = get_word(word_list)
        play(word)

if __name__ == '__main__':
    main()
