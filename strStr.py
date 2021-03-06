Implement strStr()
Easy

1236

1638

Add to List

Share
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

############# 

# split function takes two arguments (str.split(separator, maxsplit))

#maxsplit : It is a number, which tells us to split the string into maximum of provided number of times. 
#If it is not provided then there is no limit.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        s = haystack.split(needle, 1)
        if len(s) == 1:
            return -1
        else:
            return len(s[0])
