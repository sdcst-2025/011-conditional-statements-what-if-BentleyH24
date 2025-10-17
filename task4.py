#! python3

"""
Have the user enter in a sentence. 
Check to see if the word "password" is located in the sentence

Inputs:
a sentence

Outputs:
"the sentence contains password"
"the sentence does not contain password"

Examples:
Enter a sentence: I will not buy this record, it is scratched.
the sentence does not contain password

Enter a sentence: The best password is no password.
the sentence contains password
"""

password = "Takala"

sentence = input("Please write a sentence:")

if "Takala" in sentence:
    print("The sentence contains the password")
else:
    print("The sentence does not contain the password")
