column = int(input("How many columns do you want?"))
rows = int(input("How much rows do you want?"))
User_1 = int(input("Enter what symbol you want to print"))

for row in range(rows):
    for star in range(column):
        print("*", end="")

    print()

