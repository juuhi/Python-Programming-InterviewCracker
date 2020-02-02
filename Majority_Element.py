Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

####### Solution that will return the middle element as it says that element will appear more than half of the list

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]

######### Solution II #####

def majorityElement(nums):
    dict = {}
    for num in nums:
        dict[num] = dict.get(num,0) + 1
    x = max(dict, key=dict.get)
    print(x) # to get the key with maximum value
    print(dict[x]) # to get the value (the times it appears)
    
    #similarly as per the question :
    for num in nums:
        if dict[num] > len(nums)//2:
            return num


majorityElement([1,2,3,2,2])
