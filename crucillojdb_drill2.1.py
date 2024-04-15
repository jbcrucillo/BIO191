age = int(input("What is your age? "))
license = input("Do you have a fishing license in MN (yes/no)? ".lower()) == "yes"
parent_license = input("Does your parent have a fishing license (yes/no)? ".lower()) == "yes"

#It is legal to fish if you are 15 years old or less if your parent has a license. If you're at least 16 years old, you need to have your own license
legal_fishing = ((age <= 15) and (parent_license)) or ((age >= 16) and (license))

if legal_fishing:
    print ("You are legal to fish in MN.")
else:
    print ("You are not yet legal to fish in MN.")
