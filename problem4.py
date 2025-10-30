#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# has a percent difference less than 2%
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""

side1 = input("Enter one side:")
side2 = input("Enter a second side:")
side3 = input("Enter third side:")

side1 = float(side1)
side2 = float(side2)
side3 = float(side3)

sidesSorted = sorted([side1, side2, side3])

sideA = sidesSorted[0]
sideB = sidesSorted[1]
hypotenuse = sidesSorted[2]

expHypotenuse = (sideA**2+sideB**2)**0.5

upperLimit = expHypotenuse*1.02
lowerLimit = expHypotenuse*0.98

if hypotenuse >= upperLimit:
    print("This triangle is obtuse")
elif hypotenuse <= lowerLimit:
    print("This triangle is acute")
else:
    print("This is a right triangle")