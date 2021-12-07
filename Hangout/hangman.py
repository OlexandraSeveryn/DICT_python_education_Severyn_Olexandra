import random

print("""HANGMAN
The game will be available soon.""")

word_list=["python", "java", "javascript"]
guesses = 8

word_select = random.choice(word_list)
letter_list = set(word_select)

hint = list('-')*len(word_select)
while True:
    print("".join(hint))
    write = input("Input a letter: > ")

    if len(write)>1 :
        print("You have to write one symbol ")
        continue

    if write in letter_list :
        letter_list.remove(write)

        for i in range(len(word_select)) :
            if word_select[i] == write :
                hint[i] += write
    else:
        guesses -= 1
        print("That letter doesn't appear in the word")

    if len(letter_list) == 0 :
        print("You survived!")
        break
    elif guesses==0:
        print("You lost!")
        break
