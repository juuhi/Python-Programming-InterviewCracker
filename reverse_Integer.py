Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit 
signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the 
reversed integer overflows.

# The concept is to set the dlag to check for the negative number and then get the result also, check weather the result exist
# within the limit defined else return 0 

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        num = 0
        is_negative = False
        if (x < 0):
            is_negative = True
            x *= -1
        while (x > 0):
            num = x % 10
            result = result*10 + num
            x = x // 10
        if result < -2 ** 31 or result > (2 ** 31) - 1:
            return 0
        elif is_negative:
            return result * -1
        else:
            return result
