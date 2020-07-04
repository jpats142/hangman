# VARIABLES AND FUNCTIONS:

def clear_screen():
    ''' PRINTS 100 NEW LINES TO CLEAR THE SCREEN '''
    print('\n' * 100 )
    
def seperator():
    '''SEPERATES ENTRIES AND MAKES SPACE BETWEEN TURNS'''
    print('  \n =======================================\n   \n =======================================')


def board():
    ''' This will print the Gallow, and how many lives have been lost
    no user input required'''
    global lives
    
    print(f" \nThe secret word has {len(word)} characters\n ")
    print(f"You have guessed: {' '.join(emp)}")
    print(" \n \n ")
        

        
    if lives == 4:
        print('===============|\n               0\n|\n|\n|\n|\n|\n|\n===============')
    elif lives == 3:
        print('===============|\n               0\n|              |\n|\n|\n|\n|\n|\n===============' )
    elif lives == 2:
        print('===============|\n               0\n|             \|/\n       \n\n|\n|\n|\n|\n===============' )   
    elif lives == 1:
        print('===============|\n               0\n|             \|/\n|             /\n|\n|\n|\n|\n|\n===============' )
    elif lives == 0:
        print('===============|\n               0\n|             \|/\n|             / \\\n|\n|\n|\n|\n|\n===============' ) 

    else:
        print ('===============|\n|\n|\n|\n|\n|\n|\n===============')

    print("   ")
    print(f"You have {lives} lives left.")
    print("   ")

    
def start(): 
    ''' asks user if they want to play, 
    uses while loop to keep asking until we have a game

    USER ENTRY: 'Y' TO INITIATE GAME
    EXIT TO QUIT GAME'''      
    while True:

        
        question = input('Do you want to play? \n\nEnter Y to start! ').lower()
        if question == 'y' or question == 'yes':
            seperator()
            print("Great! Lets play!")
            
            break    
    
        elif question == 'exit':
            
            global exit
            exit += 1
            break

        else:
            print("Y or Yes to start, EXIT to quit. ")



def choose_players():
    ''' Option to select one of two player mode. will keep asking user until chosen

    user entry : expects 1 or 2'''

    global players
    while players != 1 or players !=2:
        players = int(input("How many players? 1 or 2?: "))

        if players == 1: 
            clear_screen() 
            break

        elif players == 2:
            clear_screen()
            break

        else:
            print("Please enter 1 or 2. ")
            continue


def random_word():
    '''For single player mode, function selects a random word from a list.
    No user input required'''
    import random
    
    global hangman        
    hangman = ['hello','bicycle', 'uniform', 'cookie', 'laptop', 'table', 'microwave', 
    'playstation','enormous', 'password','required', 'keyboard', 'style', 'distance',
    'animal', 'trousers', 'barcelona', 'pancake', 'coffee', 'fridge', 'venezuela', 
    'glasses', 'random', 'purple', 'tenerife', 'jamaica', 'monkey','beautiful']
          
    global word
    word = random.choice(hangman) # chooses random word from above list
    hangman = list(word)

    for i in word:
        emp.append('_') # underscore for every character of the random word
                
              
            

def enter_word():
    ''' Function for two player mode, allows first player to input a word. Will loop until a valid word is entered.

    User input: for now words must be single, function will only allow letters'''
    
    while True: 
        global word
        word = input('Player One, pease enter your secret word: ').lower()

        if word.isalpha(): # Loop can only be broken if the word is in the alphabet

            clear_screen()

            global hangman
            hangman = list(word)

            for i in word:
                emp.append('_') # appends empy list with underscore per letter
        
            break
        
        else:
            print("That's not a valid word, try another.")



def one_player():
    '''Function for single player gameplay'''   
    while True:

        board() # Calls board func

        global lives # lives == 5 

        # Checks if user has ran out of lives and breaks loop if lives less than 1
        if lives < 1:
            print('You are out of lives, you lose!\n \n ')
            print(f"The word was {' '.join(word)}.")   
            break
        
        # Takes user input, note user should try 1 letter at a time      
        guess = input("Please guess a letter: ").lower()

        seperator()
        
        # Checks if user input has already been tried
        if guess in Guess:
            print("You've already guessed that")      
        
        # Checks if user input is in the secret word, also records the try to avoid repetition      
        elif guess in hangman:
            print(f"Well done, {guess} is in the word.")
            Guess.append(guess)
            

            for i in range(len(hangman)): 
                character = hangman[i]  # loop to replace underscores with successful guesses 
                if character == guess:
                    emp[i] = hangman[i]
                    hangman[i] = '_'
                    
        
        # If the input hasn't been tried and isn't in the secret word, user will lose 1 life.         
        if guess not in hangman and guess not in Guess:
            lives -= 1      
            Guess.append(guess)
            print(f"Sorry, {guess} is not in the word.")

        # çhecks if the user has won, breaks loop if user has guessed the word    
        elif ' '.join(word) == ' '.join(emp):
            print (f"Well done, you've guessed it! The word was {' '.join(word)} ")
            break
    

    
def two_player():
    ''' Func for two player gameplay '''
    
    while True:

        board() # Calls board func

        global lives # lives == 5

        # Checks if user has ran out of lives and breaks loop if lives less than 1
        if lives < 1:
            print("You are out of lives, you lose!\n \n ")
            print(f"The word was {' '.join(word)}.")   
            break

        # Takes user input, note user should try 1 letter at a time      
        guess = input("Player Two, whats your guess? ")

        seperator()
        
        # Checks if user input has already been tried
        if guess in Guess:
            print("You've already guessed that")      
        
        # Checks if user input is in the secret word, also records the try to avoid repetition      
        elif guess in hangman:
            print(f"Well done {guess} is in the word.")
            Guess.append(guess)
          
            for i in range(len(hangman)):
                character = hangman[i]
                if character == guess: # loop to replace underscores with successful guesses 
                    emp[i] = hangman[i]
                    hangman[i] = '_'
                    
        # If the input hasn't been tried and isn't in the secret word, user will lose 1 life.         
        if guess not in ' '.join(emp) and guess not in Guess:
            lives -= 1      
            Guess.append(guess)
            print(f"Sorry, {guess} is not in the word.")

        # çhecks if the user has won, breaks loop if user has guessed the word  
        elif ' '.join(word) == ' '.join(emp):
            print (f"Well done, you've guessed it! The word was {' '.join(word)} ")
            break


 # THE GAME BELOW 
                   
while True:  # Loop to continue unless exit == 1
    hangman = [] #  empty list for the secret word
    Guess = [] # empty list for player guess to avoid repetition
    word = ' ' # empty string for secret word
    emp = []  # empty list to append _ in place of letters in secret word
    exit = 0 # variable for quit game loop
    lives = 5 # player has 5 lives, game on whiles lives above 0
    players = 0 # varible for number of players, while not 1 or 2 loop continues
    
    seperator() # seperates guesses 

    start() # Checks if player wants to play 

    if exit == 1:
        print("Maybe next time!")
        break # Player can end the game by entering exit


    seperator() # seperates guesses 

    choose_players() # Player selects 1 or 2 player mode    

    if players == 1: # If player selects 1, random word generated        

        random_word()
                     
        one_player()     

    elif players == 2: # If plaer selects 2, player one chooses a word

        enter_word()

        two_player()

        

    continue  # Once player has lost lives, or guessed the word loop will go back to the start.       
            
  
        
