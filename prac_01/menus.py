"""
Start
Define a function main().
get the user to enter their name and store it in a variable name.
get a variable choice to an empty string.
Enter a while loop that continues until the user enters 'Q' (quit):
Display the options:
"(H)ello"
"(G)oodbye"
"(Q)uit"
get the user to enter a choice and convert it to uppercase.
Check the user's choice:
If the choice is 'H', print "Hello" followed by the user's name.
If the choice is 'G', print "Goodbye" followed by the user's name.
If the choice is neither 'H', 'G', nor 'Q', print "Invalid choice".
Print "Finished" when the user chooses to quit.
Check if the script is being run directly (not imported):
If so, call the main() function.
End.
"""
# CODE:


def main():
    name = input("Enter name: ")

    choice = ''
    while choice != 'Q':
        print("(H)ello")
        print("(G)oodbye")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == 'H':
            print("Hello", name)
        elif choice == 'G':
            print("Goodbye", name)
        elif choice != 'Q':
            print("Invalid choice")

    print("Finished.")


if __name__ == "__main__":
    main()
