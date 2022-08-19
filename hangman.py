#A simple game of hangman
import random

def hangman():
    # From a list of words, randomly choose a word to guess.
    list_of_words = ["stuff", "word", "testing"]
    # Counter for wrong guesses.
    wrong = 0
    # This is a list with each item being a stage of the game.
    # With each wrong answer, print a line of stages.
    stages = ["",
             "__________          ",
             "|                   ",
             "|         |         ",
             "|         O         ",
             "|        /|\        ",
             "|        / \        ",
             "|                   "
            ]
    # Choosing random word.
    word = random.choice(list_of_words)
    # Turn chosen word into a list of characters.
    right_letters = list(word)
    # Representation of word space, underscores for each letter of word.
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    #While wrong guesses is less than length of stages list, run loop.
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg).lower()
        # If input is in right_letters, set char_index to the first instance of the char in list.
        # Then swap the item at that index of board with the guessed char.
        # Lastly, swap out the item at that index of right_letters with a $ to remove it from possible index search.
        if char in right_letters:
            char_index = right_letters.index(char)
            board[char_index] = char
            right_letters[char_index] = '$'
        else:
            wrong += 1
                
        print((" ".join(board)))
        # When slicing, must add 1 to compensate for last item.
        # e stands for the next row of 'stages', as marked by wrong count. Joined by newline.
        e = wrong + 1
        
        print("\n".join(stages[0: e]))
        
        # If no more blank slots remain, you guessed all the letters and win.
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
            
    if not win:
        print("\n".join(stages[0:wrong]))
        print(f"You lose! It was {word}.")
        
hangman()