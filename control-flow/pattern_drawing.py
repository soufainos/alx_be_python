def pattern_drawing():
    size = int(input("Enter the size of the pattern: "))
    checker = 0
    while checker < size:
        for i in range(size):
            print("*", end="")
        print("\n")    
        checker+=1
pattern_drawing()