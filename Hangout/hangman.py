import random

print("""HANGMAN
The game will be available soon.""")

word_list=["python", "java", "javascript"]

word_select = random.choice(word_list)

hint = ''
for i in range(0,len(word_select)):
    if i < 3:
        hint +=word_select[i]
    else :
        hint +='-'

write = input("Guess the word "+hint+"> ")
if write == word_select:
    print("You survived!")
else :
    print("You lost!")

