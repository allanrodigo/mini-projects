import random

MAX_NUMBER = 20
MAX_NUMBER_TRIALS = 5


def validations(x: int) -> bool:
    if not isinstance(x, int):
        print("Please type a valid integer next time.")
        return False
    if x < 1 or x > MAX_NUMBER:
        print(f"Please choose a number between 1 and {MAX_NUMBER}.")
        return False
    return True


def get_random_number(num: int) -> int:
    return random.randint(1, num)


if __name__ == '__main__':
    number = get_random_number(MAX_NUMBER)
    for i in range(MAX_NUMBER_TRIALS):
        try:
            attempt = int(input(f"Choose a number from 1 to {MAX_NUMBER}: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if validations(attempt):
            if attempt == number:
                print("\n")
                print(36 * "=")
                print("Correct answer! ★ Congratulations ★")
                print(36 * "=")
                break
            else:
                print("Wrong answer! Try again...\n")
        if i == MAX_NUMBER_TRIALS-1:
            print(f"Game over! The correct number was {number}.")
