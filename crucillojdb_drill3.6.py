n = int(input("Enter the side length of the square: "))

for i in range(n):
    filled_row = "*" * n

    if i == 0 or i == n - 1:
        hollow_row = "*" * n
    else:
        hollow_row = "*" + " " * (n - 2) + "*"

    print(filled_row, "\t\t", hollow_row)

    