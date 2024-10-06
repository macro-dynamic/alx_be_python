from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    """
    This function displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format the date and time
    print(f"Current date and time: {formatted_date}")

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    """
    This function calculates the future date by adding a given number of days to the current date.
    """
    current_date = datetime.now()  # Get the current date and time
    future_date = current_date + timedelta(days=days_to_add)  # Add the specified number of days
    formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the future date
    print(f"Future date: {formatted_future_date}")

# Main function to call both parts
def main():
    display_current_datetime()  # Display the current date and time
    
    # Prompt the user for the number of days to add
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days_to_add)  # Calculate and display the future date
    except ValueError:
        print("Please enter a valid integer for the number of days.")

if __name__ == "__main__":
    main()

