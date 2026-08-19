import random

# Hangman ASCII stages (0 = no wrong guess, 6 = fully hanged)
HANGMAN_STAGES = [
    """
       -----
       |   |
       |
       |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |   |
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  /
       |
    ---------
    """,
    """
       -----
       |   |
       |   O
       |  /|\\
       |  / \\
       |
    ---------
    """
]

WORD_LIST = [
    "python", "hangman", "developer", "keyboard", "function",
    "variable", "computer", "internet", "programming", "algorithm"
]


def choose_word():
    return random.choice(WORD_LIST)


def display_word(word, guessed_letters):
    """Word ko letters dekhau, guess nabhako letter lai underscore ma"""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def get_guess(guessed_letters):
    """User bata valid single letter input linu"""
    while True:
        guess = input("\nEk letter guess garnus: ").lower().strip()

        if len(guess) != 1:
            print("Kripaya EK letter matra type garnus!")
        elif not guess.isalpha():
            print("Kripaya alphabet matra type garnus!")
        elif guess in guessed_letters:
            print(f"Timile '{guess}' pahile nai guess garisakyou. Arko try garnus!")
        else:
            return guess


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("=" * 40)
    print("     HANGMAN GAME MA SWAGAT CHA!")
    print("=" * 40)

    while wrong_guesses < max_wrong_guesses:
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Galat guesses: {wrong_guesses}/{max_wrong_guesses}")
        if guessed_letters:
            print(f"Guess gareko letters: {', '.join(sorted(guessed_letters))}")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 BADHAI CHA! Timile word sahi guess garyou!")
            print(f"Word thiyo: {word.upper()}")
            break

        guess = get_guess(guessed_letters)
        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Sahi cha! '{guess}' word ma cha.")
        else:
            wrong_guesses += 1
            print(f"❌ Galat! '{guess}' word ma chaina.")

    else:
        # Loop wrong_guesses == max_wrong_guesses vayera end vayo (break bhayena)
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"\n💀 GAME OVER! Timro attempts sakiyo.")
        print(f"Word thiyo: {word.upper()}")


def main():
    play_hangman()

    while True:
        again = input("\nFeri khelne? (y/n): ").lower().strip()
        if again == 'y':
            print("\n")
            play_hangman()
        elif again == 'n':
            print("Khelisakeko ma dhanyabad! Bye 👋")
            break
        else:
            print("Kripaya 'y' ya 'n' matra type garnus.")


if __name__ == "__main__":
    main()