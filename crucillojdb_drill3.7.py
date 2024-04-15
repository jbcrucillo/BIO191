side_length = int(input("Enter the side length of the diamond: "))

for i in range(1, side_length + 1):
    print(" " * (side_length - i) + "*" * (2 * i - 1))
for i in range(side_length - 2, -1, -1):
    print(" " * (side_length - i - 1) + "*" * (2 * i + 1))


