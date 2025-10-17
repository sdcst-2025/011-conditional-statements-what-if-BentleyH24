#! python3
"""
 Have the user input a number 
 Determine if the number is positive, negative or 0 
 2 points

 Inputs:
 number

 Outputs:
 - "positive"
 - "negative"
 - "zero"

 Example:

Enter a number: 3
positive

Enter a number: -1.2
negative
"""

number = input("Enter a number:")
number = int(number)

if number < 0:
    print("The number is negative")
elif number > 0:
    print("The number is positive")
else:
    print ("The number is 0")