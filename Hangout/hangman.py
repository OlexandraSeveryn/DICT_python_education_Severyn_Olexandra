print("""HANGMAN
The game will be available soon.""")

word = "python"
write = input("Guess the word > ")
if write == word:
    print("You survived!")
else :
    print("You lost!")