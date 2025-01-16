str1 = 'ram is going to school'
words = str1.split()
print(words)

reversed = words[::-1]
reversed_sentence = " ".join(reversed)
print(reversed_sentence)
print("---------------------------------------")


str2 = "The father of the nation is Mahatma Gandhi"
words2 = str2.split()
words2[0] = words2[0].lower()
print(words2)

new_string = words2[6:] + words2[5:6] + words2[:5]
new_sentence = " ".join(new_string)
print(new_sentence)


"""Output:
['ram', 'is', 'going', 'to', 'school']
school to going is ram
---------------------------------------
['the', 'father', 'of', 'the', 'nation', 'is', 'Mahatma', 'Gandhi']
Mahatma Gandhi is the father of the nation"""