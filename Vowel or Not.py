# Write a function that takes a character (i.e. a string of length 1)
# and returns True if it is a vowel, False otherwise.

def checkVowel(val):
    if val in ('a','e','i','o','u'):
        return True
    else:
        return False

print("Enter a character")
val = input()

print(checkVowel(val))