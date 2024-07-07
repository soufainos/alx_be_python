import datetime

def display_current_datetime():
  """
  This function retrieves the current date and time and prints it in a formatted string.
  """
  current_date = datetime.datetime.now()
  formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Current date and time: {formatted_datetime}")

def calculate_future_date(number_of_days):
  """
  This function calculates the future date by adding a specified number of days to the current date.

  Args:
      number_of_days: An integer representing the number of days to add.

  Returns:
      A datetime object representing the future date.
  """
  current_date = datetime.datetime.now()
  future_date = current_date + datetime.timedelta(days=number_of_days)
  return future_date

if __name__ == "__main__":
  display_current_datetime()

  # Get user input for number of days
  while True:
    try:
      number_of_days = int(input("Enter the number of days to add to the current date: "))
      break
    except ValueError:
      print("Invalid input. Please enter an integer value.")

  # Calculate and print the future date
  future_date = calculate_future_date(number_of_days)
  formatted_future_date = future_date.strftime("%Y-%m-%d")
  print(f"Future date: {formatted_future_date}")
