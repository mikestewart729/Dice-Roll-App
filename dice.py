# dice.py

import random
import argparse
from typing import List

# Constants
DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
}
DIE_HEIGHT = len(DICE_ART[1])
DIE_WIDTH = len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = " "

def parse_input(input_string: str) -> int:
    """
    Returns 'input_string' as an integer (no limit on number). Check whether
    the user input is an integer, and if so, return an integer with the same value. 
    Otherwise, exit the program gracefully and tell the user to supply a valid value

    Args:
       input_string (str): String value representing user chosen number
          of dice to roll.
    
    Returns:
        int: Input_string converted to an integer.
    """
    if input_string.strip().isnumeric():
        return int(input_string)
    else:
        print("Please enter a whole number. Exiting program.")
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

def generate_dice_faces_diagram(dice_values: List[int]) -> str:
    """
    Create ASCII art showing the faces of each die rolled.

    Args: 
       dice_values (List[int]): Values of the rolled dice to be displayed.

    Returns:
       str: ASCII art representing the dice faces from dice_values, to be
          displayed to the user.
    """
    dice_faces = _get_dice_faces(dice_values)
    dice_faces_rows = _generate_dice_faces_rows(dice_faces)
    
    width = len(dice_faces_rows[0])
    diagram_header = " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

def _get_dice_faces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    return dice_faces

def _generate_dice_faces_rows(dice_faces):
    dice_faces_rows = []
    num_dice = len(dice_faces) 
    num_dice_rows = (num_dice - 1) // 6 + 1 # get total number of rows of dice with 6 per row
    for i in range(num_dice_rows):
        for row_idx in range(DIE_HEIGHT):
            row_components = []
            for die in dice_faces[6*i:6*i+6]:
                row_components.append(die[row_idx])
            row_string = DIE_FACE_SEPARATOR.join(row_components)
            dice_faces_rows.append(row_string)
    return dice_faces_rows

def sum_dice_rolls(roll_results: List[int]) -> int:
    """
    Returns the total value of the rolled dice.

    Args:
       roll_results (List[int]): Dice roll values to be summed

    Returns:
       int: Total value of the rolled dice.
    """
    return sum(roll_results)

def parse_user_cli_args():
    """
    Read the user command line inputs, if there are any, and adapt the program 
    according to user specifications.
    """
    parser = argparse.ArgumentParser(
        description="Rolls a user selected number of dice and displays them."
    )
    parser.add_argument(
        '-n',
        '--number',
        type=int,
        help="Number of dice to roll."
    )
    parser.add_argument(
        '-s',
        '--sum',
        action='store_true',
        help='Display the total sum of all the dice rolled.'
    )
    return parser.parse_args()

def parse_display_sum(display_sum):
    """
    Converts user input of y/n or Y/N, Yes/No, YES/NO, True/False, 0/1 to a boolean
    value and returns
    """
    display_sum = display_sum.strip().lower()
    if display_sum in {"y", "yes", "true", "1"}:
        return True
    return False

def main():
    # 0. Get command line arguments from the user, if any
    user_args = parse_user_cli_args()

    # 1. Get and validate the user's input
    if user_args.number is None:
        num_dice_input = input("How many dice do you want to roll? (Whole number) ")
        num_dice = parse_input(num_dice_input)
    else:
        num_dice = user_args.number

    # 2. Roll the dice
    roll_results = roll_dice(num_dice)
    # for debugging:
    # print(roll_results)

    # 3. Generate the ASCII art of the dice roll
    dice_face_diagram = generate_dice_faces_diagram(roll_results)

    # 4. Display the diagram
    print(f"\n{dice_face_diagram}")

    # 5. Display the sum of the dice rolls if requested
    if not user_args.sum:
        display_sum = input("Sum your dice? [y/n] ")
        sum_dice = parse_display_sum(display_sum)
    if user_args.sum or sum_dice:
        total = sum_dice_rolls(roll_results)
        print(f"\nThe total value of the dice rolls is: {total}")

if __name__ == '__main__':
    main()