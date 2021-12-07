import random

print("""HANGMAN
The game will be available soon.""")

word_list=["python", "java", "javascript"]

word_select = random.choice(word_list)
write = input("Guess the word > ")
if write == word_select:
    print("You survived!")
else :
    print("You lost!")