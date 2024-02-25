"""
Start
If the score is less than 0 or greater than 100, print "Invalid score"
Else, if the score is greater than or equal to 90, print "Excellent"
Else, if the score is greater than or equal to 50, print "Passable"
Else, print "Bad"
Define the main() function
get the user to enter a score
Print "User's result
Generate a random score using random.randint(0, 100)
Print "Random score:" followed by the random score
Print "Random result:" followed by the result obtained from calling get_result() with the random score
Check if the script is being run directly by checking __name__ against "__main__"
End
"""
# CODE:
import random


def get_result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def main():
    user_score = float(input("Enter score: "))
    print("User's result:", end=" ")
    get_result(user_score)

    # Generating a random score
    random_score = random.randint(0, 100)
    print("Random score:", random_score)
    print("Random result:", end=" ")
    get_result(random_score)


if __name__ == "__main__":
    main()

