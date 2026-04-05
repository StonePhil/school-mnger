def validate_positive_int(prompt: str) -> int:
    #loop until valid positive integer is entered
    while True:
        try:
            value = input(prompt).strip()
            val = int(value)
            if val <= 0:
                raise ValueError
            return val
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def validate_non_empty(prompt: str) -> str:
    """Loop until non-empty string is entered."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")
