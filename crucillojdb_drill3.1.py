asterisk_count = int(input('Enter an integer: '))
cnt = 1
while cnt <= asterisk_count:
    for j in range(0,cnt):
        print("*", end="")
        if (j != cnt):
            print(" ", end="")

    cnt = cnt + 1
    print()