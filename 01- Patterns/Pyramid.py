rows= int(input("Number if rows: "))

for row in range(rows):
    for space in range(rows-row):
        print(" ", end=" ")
    for star in range(row):
        print("* ", end=" ")
    print("\n")