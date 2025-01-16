# You work in a company and you are given customers number, But many customers filled wrong data, so you need to check if the number given by customer is right or not.
#
# Phone Number should match following Criteria :
#
#     Only numbers , spaces are allowed though (so few customers wrote their number with spaces.)
#
#     10 character only.

input_num = input("Enter your 10 Digit phone number: ")
cust_num = input_num.replace(" ", "")
print(cust_num)

if cust_num.isdigit() and len(cust_num)==10:
    print(f"{cust_num} number entered is Valid")
else:
    print("Please enter a valid 10 digit number")


"""Output:
Enter your 10 Digit phone number: 74  1  18  4     8 1 77
7411848177
7411848177 number entered is Valid"""

