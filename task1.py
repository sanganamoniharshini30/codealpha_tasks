import random

words = ["apple", "mango", "python", "banana", "orange"]

word = random.choice(words)

guessed = ["_"] * len(word)

chances = 6

hangman = [
    """
     -----
     |   |
         |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
         |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
         |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
    --------
    """,
    """
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    --------
    """
]

print("Welcome to Hangman Game!")

while chances > 0:

    print("\nWord:", " ".join(guessed))
    print("Remaining chances:", chances)

    guess = input("Enter a letter: ").lower()

    if guess in word:

        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess

        print("Correct Guess!")

    else:
        chances -= 1
        print("Wrong Guess!")
        print(hangman[6 - chances])

    if "_" not in guessed:
        print("\nCongratulations! You Won!")
        print("The word was:", word)
        break

else:
    print(hangman[6])
    print("\nGame Over!")
    print("The word was:", word)