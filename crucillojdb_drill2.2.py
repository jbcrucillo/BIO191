age = int(input("Please enter your age: "))
citizenship = input("Are you a natural born citizen od the U.S. (yes/no)? ".lower()) == "yes"
residency = int(input("How many years have you resided in the U.S.? "))

eligible = ((age >= 35) and citizenship and (residency >= 14))
if eligible:
    print ("You can run for president of USA")
else:
    print ("You cannot run for president of USA")


