# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

############################################# SOLUTION ########################

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    shortest = min(strs, key=len) # this
    for i, ch in enumerate(shortest):   # 0 # 1
        for other in strs:   # this # these
            if other[i] != ch:   # t != t
                return shortest[:i]   #return till location
    return shortest   # this is the case, when the full smallest string is the prefix for rest of the strings

###################### tests beelow (ignore) ####################################

# print(longestCommonPrefix(['this','these']))
# # print(longestCommonPrefix([""]))


# s = 'abc'
# print(s[:i])
