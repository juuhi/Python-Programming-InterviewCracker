#Program to check palindromem, ignoring the whitespaces (split function removes the leading and trailing spaces only)

def checkPalindrome(string):
    #print(string.split(' '))
    if (string[::-1].replace(" ", "")) == (string.replace(" ", "")):
        print("Palindrome")
    else:
        print("no")

checkPalindrome("ab cba")
checkPalindrome("testing")
checkPalindrome("race car")
