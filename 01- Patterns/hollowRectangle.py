rows= int(input("Number if rows: "))
columns= int(input("Number if columns: "))

for row in range(rows):
    for column in range(columns):
        if(row==0 or row==rows-1):
            print("*", end=" ")
        else:
            if(column==0 or column==columns-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print("\n")


