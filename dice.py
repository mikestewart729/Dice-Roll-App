# dice.py

import random
from typing import List

def parse_input(input_string: str) -> int:
    """
    Returns 'input_string' as an integer between 1 and 6. Check whether
    the user input is an integer between 1 and 6, and if so, return an 
    integer with the same value. Otherwise, exit the program gracefully
    and tell the user to supply a valid value

    Args:
       input_string (str): String value representing user chosen number
          of dice to roll.
    
    Returns:
        int: Input_string converted to an integer.
    """
    if input_string.strip() in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a value between 1 and 6. Exiting program.")
        raise SystemExit(1)

def roll_dice(num_dice: int) -> List[int]:
    """
    Simulate rolling num_dice dice and return the output.

    Args:
       num_dice (int): Number of dice to simulate rolling.

    Returns:
       List[int]: Results of the num_dice rolls in a list.
    """
    roll_results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        roll_results.append(roll)
    return roll_results

def main():
    # 1. Get and validate the user's input
    num_dice_input = input("How many dice do you want to roll? [1-6] ")
    num_dice = parse_input(num_dice_input)

    # 2. Roll the dice
    roll_results = roll_dice(num_dice)
    # for debugging:
    print(roll_results)

if __name__ == '__main__':
    main()