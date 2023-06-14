rows= int(input("Number if rows: "))

for row in range(rows):
    for columm in range(row):
        print(" ", end=" ")
    for column in range(rows-row):
        print("* ", end=" ")
    print("\n")