# Find the second maximum digit from a number

input_num = input("Enter the number you wish to evaluate: ")
max_digit = max(input_num)
print("The maximum digit in number entered is:", max_digit)

number_2 = input_num.replace(max_digit, "")
max_digit_2 = max(number_2)
print("The 2nd maximum digit in number entered is:", max_digit_2)


"""Output:
Enter the number you wish to evaluate: 7411848177
The maximum digit in number entered is: 8
The 2nd maximum digit in number entered is: 7
"""