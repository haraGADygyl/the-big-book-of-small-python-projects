import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print(f'''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com

I am thinking of a {NUM_DIGITS}-digit number with no repeated digits.
Try to guess what it is. 
Here are some clues:
When I say:   That means:
Pico          One digit is correct but in the wrong position.
Fermi         One digit is correct and in the right position.
Bagels        No digit is correct.

For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico''')

    while True:
        """ This stores the secret number the player needs to guess. """
        secret_number = get_secret_number()

        print('I have thought of a secret number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        guesses_count = 1
        while guesses_count <= MAX_GUESSES:
            guess = ''

            """ Keep looping until the player enters a valid guess. """
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Guess #{guesses_count}')
                guess = input('> ')

            clues = get_clues(guess, secret_number)
            print(clues)
            guesses_count += 1

            if guess == secret_number:
                break

            if guesses_count > MAX_GUESSES:
                print('You ran out of guesses!')
                print(f'The answer was {secret_number}')

        """ Ask the player is he wants to play again. """
        print('Do you want to play again? (yes or no)')

        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')


def get_secret_number():
    """ Returns a string made up of NUM_DIGITS unique random digits. """

    numbers = list('1234567890')
    random.shuffle(numbers)

    """ Get the first number NUM_DIGITS digits in the list for the secret number. """
    secret_number = ''
    for i in range(NUM_DIGITS):
        secret_number += str(numbers[i])

    return secret_number


def get_clues(guess, secret_number):
    """ Returns a string with the pico, fermi, bagels clues for a guess and secret number pair. """

    if guess == secret_number:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            """ A correct digit is in the correct place. """
            clues.append('Fermi')
        elif guess[i] in secret_number:
            """ A correct digit is in the incorrect place. """
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'
    else:
        """ Sort the clues into alphabetical order so their original order doesn't give information away. """
        clues.sort()
        return ' '.join(clues)


""" If the program is run (instead of imported), run the game. """
if __name__ == '__main__':
    main()

"""
Q: What happens when you change the NUM_DIGITS constant?
A: The size of the secret number changes.

Q: What happens when you change the MAX_GUESSES constant?
A: The number of tries changes.

Q: What happens if you set NUM_DIGITS to a number larger than 10?
A: An IndexError is raised at line 66:
    secret_number += str(numbers[i])
    IndexError: list index out of range

Q: What happens if you replace secret_number = get_secret_number() on line 24 with secret_number = '123'?
A: The program is still working as expected, but with a hardcoded secret_number value witch will always be '123'.

Q: What error message do you get if you delete or comment out guesses_count = 1 on line 30?
A: An UnboundLocalError is raised at line 31:
    while guesses_count <= MAX_GUESSES:
    UnboundLocalError: local variable 'guesses_count' referenced before assignment

Q: What happens if you delete or comment out random.shuffle(numbers) on line 62?
A: The numbers variable will never shuffle, so the secret_number variable will always start with 1, followed by
    NUM_DIGITS count of characters.

Q: What happens if you delete or comment out if guess == secret_number: on line 74 and return 'You got it!' on line 75?
А: After each guess entered by the player, the program will return 'You got it!' and no validation will be done.

Q: What happens if you comment out guesses_count += 1 on line 40?
A: The guesses_count variable will always be 1 and the player will have unlimited number of guesses.
"""
