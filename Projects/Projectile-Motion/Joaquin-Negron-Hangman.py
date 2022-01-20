import random
word_list = ['bucana', 'jacaguas', 'guajataka', 'fajardo', 'loco', 'bayagan', 'nigua', 'pastillo', 'cerrillos', 'daguao']

def display_hangman(tries):
    stages = ["""
                    --------
                    |    |
                    |    O
                    |   /|\\
                    |    |
                    |   / \ 
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