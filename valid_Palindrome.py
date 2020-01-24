#Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

#Note: For the purpose of this problem, we define empty string as valid palindrome.

#Example 1:

#Input: "A man, a plan, a canal: Panama"
#Output: true
#Example 2:

#Input: "race a car"
#Output: false


class Solution(object):
    def isPalindrome(self, s):
        s = ''.join(e for e in s if e.isalnum()).lower()
        if s == s[::-1]:
            return True
        else:
            return False
