# You are tasked to swap first and last characters of a string

def swap_string():
    input_str = input("Enter your string contents: ")
    first_char = input_str[0]
    last_char = input_str[-1]
    center_char = input_str[1:-1]
    output_str = last_char + center_char + first_char
    print(f"The swapped string is: '{output_str}'")

swap_string()


"""Output:
Enter your string contents: Operations
The swapped string is: 'sperationO'
"""