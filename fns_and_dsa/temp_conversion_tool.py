# Global conversion factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
FAHRENHEIT_BASE = 32

# Function to convert Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    """
    return (fahrenheit - FAHRENHEIT_BASE) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    Converts Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_BASE

# Main function for user interaction
def main():
    try:
        # Prompt the user to input a temperature
        temp = float(input("Enter the temperature to convert: "))

        # Ask if the temperature is in Celsius or Fahrenheit
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

# Call the main function
if __name__ == "__main__":
    main()
