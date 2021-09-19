An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: n = 8
Output: true
Explanation: 8 = 2 × 2 × 2
  
############################################### Solution ################################


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for x in [2, 3, 5]:
            while n % x == 0:
                n = n / x
        return n == 1


