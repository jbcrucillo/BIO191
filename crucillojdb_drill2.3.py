num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter another integer: "))
num3 = int(input("Please enter a third integer: "))

largest_odd = None

if num1 % 2 != 0:
    largest_odd = num1
elif num2 % 2 != 0 and (largest_odd is None or num2 > largest_odd):
    largest_odd = num2
elif num3 % 2 != 0 and (largest_odd is None or num3 > largest_odd):
    largest_odd = num3
    
if largest_odd is not None:
    print("The largest odd integer is:", largest_odd)
else:
    print("None of the integers are odd.")