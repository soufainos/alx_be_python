task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" | "medium" | "low": 
        reminder =f"Reminder: {task} is a {priority} priority task that requires immediate attention today!"
        low_reminder = f"Note: {task} is a {priority} priority task. Consider completing it when you have free time."

if time_bound == "yes":
    print(reminder)
else:
    print(low_reminder)



