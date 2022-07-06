"""Simulation of the probabilities of a dice"""
import random


def roll_dice(number_of_rolls):
    """Simulation of a dice of six faces 1-6"""
    sequence_of_rolls = []  # store each roll of dice(6 faces) cube

    for _ in range(number_of_rolls):
        roll = random.choice([1, 2, 3, 4, 5, 6])
        sequence_of_rolls.append(roll)

    return sequence_of_rolls


def main(number_of_rolls, number_of_tries):
    #  1. Generating the sequences of rolls
    rolls = []  # store the result of a n number of rolls
    for _ in range(number_of_tries):  # run the simulation n times
        sequence_of_rolls = roll_dice(number_of_rolls)
        rolls.append(sequence_of_rolls)

    # 2. Calculating the probabilities
    # probability of get at least a 1
    rolls_with_1 = 0
    for roll in rolls:
        if 1 in roll:
            rolls_with_1 += 1

    # probabilities_rolls_with_1 = rolls_with_1 / number_of_tries
    # print(
    #     f'Probability of get at least a 1 in {number_of_tries} rolls = {probabilities_rolls_with_1}')

    # probability of don't get a 1
    rolls_with_not_1 = 0
    for roll in rolls:
        if 1 not in roll:
            rolls_with_not_1 += 1

    probabilities_rolls_with_not_1 = rolls_with_not_1 / number_of_tries
    print(
        f'Probability of do not get a 1 in {number_of_tries} rolls = {probabilities_rolls_with_not_1}')


if __name__ == "__main__":
    number_of_rolls = int(input('How many times roll the dice:'))
    number_of_tries = int(input('How many times will run the simulation:'))

    main(number_of_rolls, number_of_tries)
