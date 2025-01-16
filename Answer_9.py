# Take a String from user consisting only alphabets and spaces, and count How many Consonants and Vowels are in the string.

take_string = input("Enter the string: ")
take_string = take_string.replace(" ", "")
vowels = "aeiouAEIOU"
vowels_count = 0
consonants_count = 0

for char in take_string:
    if char.isalpha():
        if char in vowels:
            vowels_count += 1
        else:
            consonants_count += 1
    else:
        print("Please enter a string with Alphabets only")

print(f"Number of vowels: {vowels_count}")
print(f"Number of consonants: {consonants_count}")


"""Output:
Enter the string: The quick brown fox jumps over the lazy dog
Number of vowels: 11
Number of consonants: 24
"""