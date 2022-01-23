import random
import sys

# Dictionary of words and meaning.
dictionary = {'Degust': 'To taste with relish or care',
              'Pogonip': 'A dense fog of suspended ice particles',
              'Muscarine': 'A highly toxic organic compound',
              'Benthos': 'The bottom of a sea or lake, especially at considerable depth',
              'Euhemerism': 'A theory attributing the origin of the gods to the deification of historical heroes',
              'Luculent': 'Easily understood, clear',
              'Tuff': 'A rock composed of compacted volcanic ash',
              'Xiphoid': 'Having the shape of a sword',
              'Yarborough': 'A hand of cards with no card more than a nine',
              'Ulotrichous': 'Having wiry or wooly hair',
              }


def guess_word():
    # Welcome's the player.
    print("GUESS THE WORD GAME.")
    print("You're welcome! \n"
          "Would you like to play? Yes or No")

    # Checks if the user has entered a valid reply.
    answer = input().lower()
    while answer != "yes" and answer != 'no':
        print("Enter yes or no")
        answer = input().lower()
    if answer == 'yes':
        print("let's go! ")
    else:
        if answer == 'no':
            print("Bye!")
            sys.exit()

    # Creates a list of the words.
    words = []
    for key in dictionary:
        words.append(key)
    print("Guess the word!")

    trials = 5  # Amount of guess.
    got_correct = 0  # number of correct answer
    total_guess_taken = 0

    # Main game loop.
    while True:
        total_guess_taken += 1

        random_options = random.sample(words, 3)  # selects 3 words from the list without repetition.
        word = random.choice(random_options)  # Pick a random word from list to be main word.

        print(f"\nThis is the meaning of the word: \n{dictionary[word]} \n"
              "What is the word? ")
        print(random_options)  # Print's the answer options
        player_answer = input().lower()  # Stores player's input.

        # Checks if player guess is correct or wrong.
        if player_answer != word.lower():
            trials -= 1
            print("WRONG!")
            print(f"The word was {word}")

        else:
            if player_answer == word.lower():
                got_correct += 1
                print("Correct!, You guessed the word!")

        if trials == 0:
            print("\nGAME END \n"
                  "Out of tries")
            print(f"You got {got_correct} / {total_guess_taken}.")
            sys.exit()


guess_word()
