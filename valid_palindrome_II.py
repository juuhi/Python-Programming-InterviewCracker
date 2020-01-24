Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:

Input: "aba"
Output: True
Example 2:

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:

The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

# This is using the two pointer solution :

class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                one, two = s[i:j], s[i+1:j+1]
                return one == one[::-1] or two == two[::-1]
            i, j = i+1, j-1
        return True
