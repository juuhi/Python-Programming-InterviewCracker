# Define a function is_palindrome() that recognizes palindromes (i.e. words that look the
#same written backwards). For example, is_palindrome("radar") should return True.

def is_palindrome(text):
    return text == text[::-1]

print("Enter the text")
text = input()
print("output is " +str(is_palindrome(text)))

"""def is_palindrome(text): (complexity increses using if, else condition)
    text1 = text[::-1]
    if text1==text:
        return True
    else:
        return False

print("Enter the text")
text = input()
print("Output is " + str(is_palindrome(text)))"""
