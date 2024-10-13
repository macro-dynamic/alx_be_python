def safe_divide(numerator, denominator):
    """
    Performs division, handling potential errors:
    - Division by Zero: catches ZeroDivisionError
    - Non-numeric Input: catches ValueError for non-numeric inputs
    Returns appropriate messages for errors or the result for successful division.
    """
    try:
        # Attempt to convert arguments to floats
        numerator = float(numerator)
        denominator = float(denominator)
        
        # Perform division
        result = numerator / denominator
        return f"The result of the division is {result:.1f}"
    
    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handle non-numeric inputs
        return "Error: Please enter numeric values only."



import sys
from robust_division_calculator import safe_divide

def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
