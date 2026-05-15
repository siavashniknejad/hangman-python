word_list = ["python", "hangman", "programming", "challenge", "developer"]
import random
word = random.choice(word_list)
print  (word)
# character = list(word)
guessed_letters = []
while True : 
    guess_letter = input("Guess a letter:")
    guessed_letters.append(guess_letter)   
    count_char = len(word)
    for i in range(count_char) :
        if word[i] in guessed_letters :
            print (word[i], end=" ")
        else :
            print("-", end=" ") 
    print()
