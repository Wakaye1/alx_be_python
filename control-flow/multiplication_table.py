# multiplication_table.py

def print_multiplication_table():
    try:
        # Prompt the user for a number
        number = int(input("Enter a number to see its multiplication table: "))

        # Generate and print the multiplication table
        for i in range(1, 10 + 1):
            product = number * i
            print(f"{number} * {i} = {product}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Main function to execute the script
if __name__ == "__main__":
    print_multiplication_table()
