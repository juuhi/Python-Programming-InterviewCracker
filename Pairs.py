# Given N integers, count the number of pairs of integers whose difference is K.
# Sample Input
#
# 5 2
# 1 5 3 4 2
# Sample Output
#
# 3

import sys

def pairs(k, arr):
    count = 0
    s = set(arr)    #this will reduce the complexity to O(1), if it traverse to the list it will be O(n)
    for i in s:
        if i+k in s:
            count += 1
    return count
    # Complete this function

print pairs (2,[3,2,1,4,6])

# print pairs(3,2)
if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = pairs(k, arr)
    print(result)