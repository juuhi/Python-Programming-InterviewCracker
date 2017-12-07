# Write a function find_longest_word() that takes a list of words and returns the length of the longest one.

def find_longest_word(text):
    return max(text.split(), key = len)
print("Enter the words to test")
text = input()
print("The longest word is of length " +str(len(find_longest_word(text))))