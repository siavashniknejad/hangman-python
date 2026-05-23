import random
word_list = ["python", "hangman", "programming", "challenge", "developer"]
word = random.choice(word_list)
print(word)
guessed_letters = []
while True:
    guess_letter = input("Guess a letter:")
    guessed_letters.append(guess_letter)
    count_char = len(word)
    all_guessed = True
    for i in range(count_char):
        if word[i] in guessed_letters:
            print(word[i], end=" ")
        else:
            print("-", end=" ")
            all_guessed = False
    print()
    if all_guessed:
        print("You win!")
        break
