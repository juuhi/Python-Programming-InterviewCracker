Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

class Solution:
    def countPrimes(self, n) -> int:
        if n < 3:
            return 0
        s = [1] * n
        s[0] = s[1] = 0
        for i in range(2, int(n ** 0.5) + 1):  # 2 to 3 inclusive for n=10 range(2,4)
            if s[i] == 1: # boolean condition to check 1 at that location
                s[i * i:n:i] = [0] * len(s[i * i:n:i]) # s[4:10:2] = [0] * 3, s[9:10:3] = [0]*1
        return sum(s)
