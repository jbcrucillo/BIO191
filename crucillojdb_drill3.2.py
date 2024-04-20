row_count = 3
col_count = 5

for i in range(0,row_count):
    for j in range(0,col_count):
        if j%2 == 0:
            print("*", end="")
        else:
            print("-", end="")

    print()