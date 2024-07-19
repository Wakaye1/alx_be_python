# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform the division
        result = num / denom

        # Return the result if successful
        return result

    except ValueError:
        # Catching non-numeric inputs
        return "Error: Please enter numeric values only."

    except ZeroDivisionError:
        # Catching division by zero
        return "Error: Cannot divide by zero."
