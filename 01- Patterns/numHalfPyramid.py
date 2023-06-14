rows= int(input("Number if rows: "))

for row in range(rows):
    for column in range(row):
        print(column+1, end=" ")
    print("\n")