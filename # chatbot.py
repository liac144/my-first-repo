# chatbot.py

# Simple chatbot to interact with the user and collect basic information.
# This bot will ask the user's name, date of birth, and hobbies.

def ask_name():
    """Function to ask the user's name."""
    while True:
        try:
            # Asking the user for their name
            name = input("What's your name? ")
            if not name:
                raise ValueError("Name can't be empty. Please enter your name.")
            return name
        except ValueError as e:
            # Handling case where the input is invalid (empty name)
            print(e)

def ask_date_of_birth():
    """Function to ask the user's date of birth."""
    while True:
        try:
            # Asking the user for their date of birth in format YYYY-MM-DD
            dob = input("What's your date of birth? (YYYY-MM-DD) ")
            # Try to split and validate the input format
            year, month, day = map(int, dob.split('-'))
            # Check if the year, month, and day are within valid ranges
            if not (1 <= month <= 12):
                raise ValueError("Month should be between 1 and 12.")
            if not (1 <= day <= 31):
                raise ValueError("Day should be between 1 and 31.")
            return dob
        except ValueError as e:
            # Handle invalid date format or out-of-range values
            print(f"Invalid date format or values. Please try again. ({e})")
        except Exception as e:
            # Handle other exceptions
            print(f"Something went wrong: {e}")

def ask_hobbies():
    """Function to ask the user for their hobbies."""
    while True:
        try:
            # Asking the user to list their hobbies
            hobbies = input("What are your hobbies? (Separate with commas) ")
            # Check if the input is empty
            if not hobbies:
                raise ValueError("Hobbies can't be empty. Please list your hobbies.")
            # Split hobbies by commas and remove any leading/trailing spaces
            hobby_list = [hobby.strip() for hobby in hobbies.split(',')]
            return hobby_list
        except ValueError as e:
            # Handle empty hobbies input
            print(e)

def main():
    """Main function to run the chatbot interaction."""
    print("Hello! I am your friendly chatbot.")
    
    # Ask for the user's name
    name = ask_name()
    
    # Ask for the user's date of birth
    dob = ask_date_of_birth()
    
    # Ask for the user's hobbies
    hobbies = ask_hobbies()

    # Print out the gathered information
    print("\nThanks for sharing, here is the information I collected:")
    print(f"Name: {name}")
    print(f"Date of Birth: {dob}")
    print(f"Hobbies: {', '.join(hobbies)}")

if __name__ == "__main__":
    # Run the main chatbot function
    main()
