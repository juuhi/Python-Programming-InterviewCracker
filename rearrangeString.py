# Given a string containing uppercase alphabets and integer digits (from 0 to 9), the task is to print the alphabets in the order followed by the sum of digits.
# 
# Input:
# The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains a string with uppercase alphabets and integer digits.
# 
# Output:
# Print alphabets in the order followed by the sum of digits.
# 
# Constraints:
# 1<=T<=10^5
# 1<=length of string<=10^5
# 
# Example:
# Input:
# 2
# AC2BEW3
# ACCBA10D2EW30
# 
# Output:
# ABCEW5
# AABCCDEW6
# 
# ** For More Input/Output Examples Use 'Expected Output' option **

def rearrangeArray(string):
     # if character -> sort , else isdigit() , s = s+y , string + str(y)
    sum = 0 # check for the initiation of the string
    new_str = ''
    for i in string:
        if i.isdigit():
            sum = sum + int(i)  #check for the int of the i 
        else:
            x = sorted(string)
            new_str = ''.join([i for i in x if not i.isdigit()])
    return new_str+str(sum)

print(rearrangeArray("AB3C1D"))

#
# s = "ABC12D"
# print(sorted(s))
