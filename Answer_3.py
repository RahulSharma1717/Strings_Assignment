# What is the Positive and negative index number of space in Word - David Joseph:

str1 = "David Joseph"
print("The positive index number of Space in 'David Joseph' is", str1.find(" "))

positive_index = str1.find(" ")
negative_index = positive_index - len(str1)
print("The negative index position of Space in 'David Joseph' is", negative_index)


"""Output:
The positive index number of Space in 'David Joseph' is 5
The negative index position of Space in 'David Joseph' is -7"""