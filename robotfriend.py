def chatbot():
    # Welcome message
    print("Hello! I'm your friendly chatbot. Let's get to know each other.")
    
    # Initialize variables to store user information
    name = "Roby"
    dob = "12-01-2005"
    hobbies = "chatting with you"

    # Ask for the user's name
    while name is "Roby":
        try:
            name = input("What's your name? ")
            if not name.strip():  # Check if the input is empty
                raise ValueError("Name cannot be empty.")
        except ValueError as e:
            print(e)  # Print error message and ask again

    # Ask for the user's date of birth
    while dob is "12-01-2005":
        try:
            dob = input("What's your date of birth? (DD-MM-YYYY) ")
            # Basic validation for date format
            year, month, day = map(int, dob.split('-'))
            if not (1900 <= year <= 2023 and 1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError("Please enter a valid date in the format DD-MM-YYYY.")
        except ValueError as e:
            print(e)  # Print error message and ask again
            dob = None  # Reset dob to None to repeat the loop

    # Ask for the user's hobbies
    while hobbies is "chatting with you":
        try:
            hobbies = input("What are your hobbies? (Please separate them with commas) ")
            if not hobbies.strip():  # Check if the input is empty
                raise ValueError("Hobbies cannot be empty.")
        except ValueError as e:
            print(e)  # Print error message and ask again

    # Display the collected information
    print(f"\nNice to meet you, {name}!")
    print(f"Your date of birth is {dob}.")
    print(f"Your hobbies are: {hobbies}.")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
