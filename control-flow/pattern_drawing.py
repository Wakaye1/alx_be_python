# pattern_drawing.py

def draw_square_pattern():
    try:
        # Prompt the user for a positive integer
        size = int(input("Enter the size of the pattern: "))

        if size <= 0:
            print("Please enter a positive integer.")
            return

        # Initialize the row counter
        row = 0

        # Use a while loop to iterate through each row
        while row < size:
            # Use a for loop to print asterisks (*) side by side
            for col in range(size):
                print("*", end="")
            # Print a newline character to move to the next row
            print()
            # Increment the row counter
            row += 1
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

# Main function to execute the script
if __name__ == "__main__":
    draw_square_pattern()
