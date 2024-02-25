"""
Start
Define a function get_password() to get the user to enter a password without storing it
get the user to enter their password
Define the main() function
Call the get_password() function to get the user for their password
Print a message indicating that the password was entered successfully
Check if the script is being run directly by checking __name__ against "__main__"
If it is, call the main() function
End
"""
# CODE:


def get_password():
    input("Enter your password: ")


def main():
    get_password()
    print("Password entered successfully.")


if __name__ == "__main__":
    main()


