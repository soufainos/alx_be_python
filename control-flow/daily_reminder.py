def reminder():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    sensitive_reminder = f"Note: {task} is a {priority} priority task. Consider completing it when you have free time."
    reminder = f"Note: {task} is a {priority} priority task. Consider completing it when you have free time."
    match priority:
        case "high": 
            if time_bound == "yes":
                print(sensitive_reminder)
            else:
                print(reminder)
        case "medium": 
            if time_bound == "yes":
                print(sensitive_reminder)
            else:
                print(reminder)
        case "low": 
            if time_bound == "yes":
                print(sensitive_reminder)
            else:
                print(reminder)
reminder()
