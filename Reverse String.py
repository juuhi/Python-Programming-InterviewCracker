# Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string "gnitset ma I".

def reverse(string):
    return string[::-1]

print('Enter the string')
string = input()
print(reverse(string))