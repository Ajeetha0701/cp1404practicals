"""

"""
# CODE:
import score

# Constants
MIN_SCORE = 0
MAX_SCORE = 100


def get_valid_score():
    while True:
        try:
            score_input = float(input("Enter a score (0-100): "))
            if MIN_SCORE <= score_input <= MAX_SCORE:
                return score_input
            else:
                print("Score must be between 0 and 100 inclusive.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def print_result(score_value):
    result = score.get_result(score_value)
    print("Result:", result)


def show_stars(score_value):
    print("Stars:", "*" * int(score_value))


def main():
    score_value = get_valid_score()

    while True:
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score_value = get_valid_score()
        elif choice == "P":
            print_result(score_value)
        elif choice == "S":
            show_stars(score_value)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
