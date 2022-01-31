# dice.py

import random
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
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string = DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    return dice_faces_rows

def main():
    # 1. Get and validate the user's input
    num_dice_input = input("How many dice do you want to roll? [1-6] ")
    num_dice = parse_input(num_dice_input)

    # 2. Roll the dice
    roll_results = roll_dice(num_dice)
    # for debugging:
    # print(roll_results)

    # 3. Generate the ASCII art of the dice roll
    dice_face_diagram = generate_dice_faces_diagram(roll_results)

    # 4. Display the diagram
    print(f"\n{dice_face_diagram}")

if __name__ == '__main__':
    main()