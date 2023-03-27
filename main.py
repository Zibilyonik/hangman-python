import random

word_tuple = ("python", "java", "swift", "javascript")

def choose_word():
    return random.choice(word_tuple)

def print_intro():
    print("H A N G M A N \n")


def print_word(word):
    print("".join(word))

def main():
    lives = 8
    word = choose_word()
    used_letters = []
    guessed = ["-"] * len(word)
    print_intro()
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
                return
        
        elif letter in guessed:
            print("No improvements. \n")
            lives -= 1
        else:
            lives -= 1
            print("That letter doesn't appear in the word \n")
    print("You lost!")

if __name__ == "__main__":
    main()