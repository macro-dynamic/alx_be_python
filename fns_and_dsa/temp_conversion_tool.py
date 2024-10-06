# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in Fahrenheit.

    Returns:
        float: Temperature in Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert a temperature from Celsius to Fahrenheit.

    Args:
        celsius (float): Temperature in Celsius.

    Returns:
        float: Temperature in Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    # Prompt user to enter a temperature and specify its unit
    temperature = input("Enter the temperature to convert: ")
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    # Validate user input
    try:
        temperature = float(temperature)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    # Convert temperature based on user input
    if unit.upper() == "C":
        converted_temperature = convert_to_fahrenheit(temperature)
        print(f"{temperature:.1f}°C is {converted_temperature:.1f}°F")
    elif unit.upper() == "F":
        converted_temperature = convert_to_celsius(temperature)
        print(f"{temperature:.1f}°F is {converted_temperature:.1f}°C")
    else:
        raise ValueError("Invalid unit. Please enter C or F.")

if __name__ == "__main__":
    main()
