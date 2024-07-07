# match_case_calculator.py

def calculator():
    try:
        # Prompt the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Ask for the type of operation
        operation = input("Choose the operation (+, -, *, /): ").strip()

        # Perform the calculation using match case
        match operation:
            case '+':
                result = num1 + num2
                print(f"The result is {result}.")
            case '-':
                result = num1 - num2
                print(f"The result is {result}.")
            case '*':
                result = num1 * num2
                print(f"The result is {result}.")
            case '/':
                if num2 != 0:
                    result = num1 / num2
                    print(f"The result is {result}.")
                else:
                    print("Error: Division by zero is not allowed.")
            case _:
                print("Invalid operation. Please choose one of the following: +, -, *, /.")
    except ValueError:
        print("Invalid input. Please enter numeric values for the numbers.")

# Main function to execute the script
if __name__ == "__main__":
    calculator()
