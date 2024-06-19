salary = int(input("Enter your monthly income: "))
expenses = int(input("Enter your total monthly expenses: "))
savings = salary - expenses
yearly = int(savings * 12 + (savings * 12 * 0.05))
print("Your monthly savings are $%s." % savings)
print("Projected savings after one year, with interest, is: $%s." % yearly)