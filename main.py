import random

word_tuple = ("python", "java", "swift", "javascript")
print("""
H A N G M A N
""")
chosen_word = random.choice(word_tuple)
if input("Guess the word " + chosen_word[:3] + "-" * (len(chosen_word) - 3) + ":") == chosen_word:
    print("You survived!")
else:
    print("You lost!")
