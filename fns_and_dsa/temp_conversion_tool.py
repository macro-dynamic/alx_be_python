# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_BASE = 32

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    This function converts a Fahrenheit temperature to Celsius.
    """
    return (fahrenheit - FAHRENHEIT_BASE) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    This function converts a Celsius temperature to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_BASE

# Main function for user interaction
def main():
    try:
        # Get the temperature from the user
        temp = float(input("Enter the temperature to convert: "))
        
        # Get the unit from the user
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            # Convert Celsius to Fahrenheit
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

# Call the main function when the script is executed
if __name__ == "__main__":
    main()

