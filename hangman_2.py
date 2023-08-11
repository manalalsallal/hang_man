import random

print ("play hangman")

def hangman():
    words = ["python", "java script", "html", "css"]
    word = random.choice(words)
    guessed_letters = []
    returns = 10

    while returns > 0:
        guessed_word = ""
        for letter in word:
            if letter in guessed_letters:
                guessed_word += letter
            else:
                guessed_word += "_"

        if guessed_word == word:
            print(" You are Win ")
            break

        print(guessed_word)

        guess = input("\n please Enter letter :  ")
      
        if guess in word:
            guessed_letters.append(guess)
            print("true")
        else:
            returns -= 1
            print(f" Wrong still {returns} returns.")

    if returns == 0:
        print(f"You loss")

hangman()
