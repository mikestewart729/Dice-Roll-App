# dice.py

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

def main():
    # 1. Get and validate the user's input
    num_dice_input = input("How many dice do you want to roll? [1-6] ")
    num_dice = parse_input(num_dice_input)

if __name__ == '__main__':
    main()