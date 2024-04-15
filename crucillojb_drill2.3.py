def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime_numbers(n):
    prime_count = 0
    num = 2
    while prime_count < n:
        if is_prime(num):
            print(num, end=" ")
            prime_count += 1
        num += 1

n = int(input("Input n: "))
print("The first", n, "prime numbers are:")
prime_numbers (n)

