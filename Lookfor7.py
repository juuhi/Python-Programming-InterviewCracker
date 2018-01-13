"""Return the sum of the numbers in the array,
except ignore sections of numbers starting with a 6 and
extending to the next 7 (every 6 will be followed by at least one 7).
Return 0 for no numbers."""
# sum67([1, 2, 2]) → 5
# sum67([1, 2, 2, 6, 99, 99, 7]) → 5
# sum67([1, 1, 6, 7, 2]) → 4

# The first code is implemented using the while loop (drawback is the complexity)
def skip67(nums):
    total = 0
    i = 0
    flag = True
    while i<len(nums):
        if nums[i] == 6:
            while nums[i]!=7:
                i=i+1
            i=i+1
        else:
            total = total+nums[i]
            i=i+1
    return total

print skip67([2,3,4,5,6,13,12,7,2])
print skip67([1, 2, 2])
print skip67([1, 2, 2, 6, 99, 99, 7])
print skip67([1, 1, 6, 7, 2])

# Function sum67 is implemented using Flag indicator (more efficient as the complexity is O(n))

def sum67(nums):
    record = True
    total = 0

    for n in nums:
        if n == 6:
            record = False

        if record:
            total += n

        if n == 7:
            record = True

    return total
print sum67([6,13,7,12,7,2])
print sum67([1, 2, 2])
print sum67([1, 2, 2, 6, 99, 99, 7])
print sum67([1, 1, 6, 7, 2])