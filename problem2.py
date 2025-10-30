#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"

number = input("Enter a number:")
number = float(number)

if number == int(number):
    print(f"{number} is an integer")
else:
    print(f"{number} is not an integer")