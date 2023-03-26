import random

word_tuple = ("python", "java", "swift", "javascript")
print("""
H A N G M A N
""")
if input("Guess the word:") == random.choice(word_tuple):
    print("You survived!")
else:
    print("You lost!")