def multiplication_table():
    number = int(input("Enter a number to see its multiplication table: "))
    for numb in range(1, 11):
        Z = numb * number
        print(f"{number} * {numb } = {Z}")
multiplication_table()