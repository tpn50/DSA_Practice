rows = int(input("Number of rows: "))

for row in range(rows):
    for coloumn in range(rows-row):
        print(coloumn+1, end="")
    print("\n")