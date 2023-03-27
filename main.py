import random

word_tuple = ("python", "java", "swift", "javascript")

def choose_word():
    return random.choice(word_tuple)

def print_intro():
    print("H A N G M A N \n")


def print_word(word):
    print("".join(word))
    
def play_game():
    lives = 8
    word = choose_word()
    used_letters = []
    guessed = ["-"] * len(word)
    while lives > 0:
        input_valid = False
        print_word(guessed)
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("Please, input a single letter.\n")
        elif letter.lower() != letter or not letter.isalpha():
            print("Please, enter a lowercase letter from the English alphabet.\n")
        elif letter in used_letters:
            print("You've already guessed this letter.\n")
        else:
            input_valid = True
            used_letters.append(letter)
        if not input_valid:
            continue
        if letter in word and letter not in guessed:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
            print("\n")
            if "-" not in guessed:
                print("You guessed the word {}!".format(word))
                print("You survived!")
                return True
        
        elif letter in guessed:
            print("No improvements. \n")
            lives -= 1
        else:
            lives -= 1
            print("That letter doesn't appear in the word \n")
    print("You lost!")
    return False
    
def print_results(win, loss):
    print("You won: {} times.\nYou lost: {} times.".format(win, loss))
    
def print_menu():
    wins = 0
    losses = 0
    while True:
        choice = input("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
        if choice == "play":
            if play_game():
                wins += 1
            else:
                losses += 1
        elif choice == "exit":
            return False
        elif choice == "results":
            print_results(wins, losses)
        else:
            print("Invalid choice. Please, try again.")

def main():
    print_intro()
    while True:
        if not print_menu():
            return
    


if __name__ == "__main__":
    main()