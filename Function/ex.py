# def reverse_string(s):
#     return s[::-1]

# # Test the function
# print(reverse_string("hello"))  



def contains_vowel(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    for char in sentence:
        if char in vowels:
            return True
    return False

# Example usage
sentence = input("Enter a sentence: ")
if contains_vowel(sentence):
    print("The sentence contains at least one vowel.")
else:
    print("No vowels found in the sentence.")





