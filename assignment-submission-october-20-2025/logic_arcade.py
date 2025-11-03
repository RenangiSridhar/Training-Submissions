import random

# ===============================
# Game 1: FizzBuzz
# ===============================
def fizzbuzz():
    print("\n=== FizzBuzz Challenge ===")
    try:
        n = int(input("Enter the number range (e.g. 50): "))
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
        print("FizzBuzz complete.\n")
    except ValueError:
        print("Invalid input. Please enter a number.\n")


# ===============================
# Game 2: Number Guessing Game
# ===============================
def number_guessing_game():
    print("\n=== Number Guessing Game ===")
    secret_number = random.randint(1, 20)
    attempts = 0

    print("I'm thinking of a number between 1 and 20.")
    print("Try to guess it!")

    while True:
        guess = input("Enter your guess (or 'exit' to quit): ")
        if guess.lower() == 'exit':
            print(f"The secret number was {secret_number}. Exiting game...\n")
            break

        if not guess.isdigit():
            print("Please enter a valid number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess == secret_number:
            print(f"Correct! The number was {secret_number}. You guessed it in {attempts} attempts.\n")
            break
        elif guess < secret_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")


# ===============================
# Game 3: Pattern Printer
# ===============================
def pattern_printer():
    print("\n=== Pattern Printer ===")
    print("Choose a pattern:")
    print("1. Right Triangle")
    print("2. Pyramid")

    choice = input("Enter your choice (1/2): ")

    if choice not in ["1", "2"]:
        print("Invalid choice.\n")
        return

    try:
        rows = int(input("Enter number of rows: "))
    except ValueError:
        print("Invalid input. Please enter a number.\n")
        return

    if choice == "1":
        for i in range(1, rows + 1):
            print("*" * i)
    elif choice == "2":
        for i in range(1, rows + 1):
            print(" " * (rows - i) + "*" * (2 * i - 1))

    print("Pattern complete.\n")


# ===============================
# Main Menu
# ===============================
def main():
    print("Python Logic Arcade")
    print("===================")

    while True:
        print("\nChoose an activity:")
        print("1. FizzBuzz")
        print("2. Number Guessing Game")
        print("3. Pattern Printer")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            fizzbuzz()
        elif choice == "2":
            number_guessing_game()
        elif choice == "3":
            pattern_printer()
        elif choice == "4":
            print("Exiting program. Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
