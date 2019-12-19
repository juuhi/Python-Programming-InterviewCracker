Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

#---------------------------------------------------------------------

#1st: Using the inbuild functions

def moveZeroes(list):
    for e in range(0, len(list)):
        if e == 0:
            list.remove(e)
            list.append(e)
    return list

print(moveZeroes([1,2,3,4,0,1]))

#2nd: Using loops

def moveZeroes(list):
    count = 0
    n = len(list)
    for i in range(0, len(list)):
        if list[i] != 0:
            list[count] = list[i]
            count += 1
    while count < n:
        list[count] = 0
        count += 1
    return list

print(moveZeroes([1,0,2,3,0]))
