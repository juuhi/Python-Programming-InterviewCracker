"""Write a function that takes a character (i.e. a
string of length 1) and returns True if it is a vowel,
False otherwise."""

def vowel_or_not(string):
    if string in ('a','e','i','o','u'):
        return True
    else:
        return False

print('Enter a string')
string = input()
print(vowel_or_not(string))