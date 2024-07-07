# daily_reminder.py

def daily_reminder():
    # Prompt the user for task description
    task = input("Enter your task: ").strip()

    # Prompt the user for task priority
    priority = input("Priority (high/medium/low): ").strip().lower()

    # Prompt the user if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

    # Initialize the reminder message
    reminder = f"Reminder: '{task}' is a {priority} priority task"

    # Use a Match Case statement for priority
    match priority:
        case "high":
            reminder += " that requires immediate attention."
        case "medium":
            reminder += "."
        case "low":
            reminder += "."
        case _:
            print("Invalid priority level. Please choose high, medium, or low.")
            return

    # Use an if statement to check if the task is time-bound
    if time_bound == "yes":
        reminder += " It is time-sensitive and requires immediate attention today!"
    elif time_bound != "no":
        print("Invalid input for time-bound. Please enter yes or no.")
        return

    # Print the customized reminder
    print(reminder)

# Main function to execute the script
if __name__ == "__main__":
    daily_reminder()
