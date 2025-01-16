# You work in a bank, You are tasked to create a pin with the help of their customer name and birthyear

def pin_generation(name, birth_date):
    pin_1 = name.split(' ')[0].title()
    pin_2 = birth_date[-4:]
    pin = pin_1 + pin_2
    print(pin)

name = input("Please enter your full name: ")
birth_date = input("Please enter your date of birth in DD-MM-YYYY format: ")
pin_generation(name, birth_date)


"""Output:
Please enter your full name: rahul sharma
Please enter your date of birth in DD-MM-YYYY format: 20-10-1989
Rahul1989
"""