# Check if a string is palindrome or not. Palindrome is a string that does not change even if you reverse it.

def check_palindrome(string):
    reverse_string = string[::-1]
    print(reverse_string)
    if string == reverse_string:
        print(f"The word '{string}' is a Palindrome")
    else:
        print(f"The word '{string}' is not a Palindrome")

string = input("Please enter a word: ").lower()
check_palindrome(string)


"""Output:
Please enter a word: Racecar
racecar
The word 'racecar' is a Palindrome
"""