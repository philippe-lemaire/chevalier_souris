import random


def roll(dice):
    """dice is a string in the shape of 'd6' or '3d4'"""
    if dice[0].isdigit():
        n_dice = int(dice[0])
        dice = dice[1:]
    else:
        n_dice = 1
    size = int(dice[1:])
    res = [random.randint(1, size) for die in range(n_dice)]
    return sum(res)


def find_key(roll, table):
    """Finds the lowest valid key in a dict where the keys are integers"""
    for key in table:
        if key <= roll:
            candidate = key
    return candidate


if __name__ == "__main__":
    print(roll("3d6"))
