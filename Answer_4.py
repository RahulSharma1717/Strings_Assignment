# How to get the first character in upper case from the name inputted by the User. For  example :
#
#
# name : 'david Joseph'
#
# Output : D

input_str = input("Enter your name: ")
first_char = input_str[0]
output = first_char.upper()
print("The first character of name entered:", output)


"""Output:
Enter your name: rahul sharma
The first character of name entered: R
"""