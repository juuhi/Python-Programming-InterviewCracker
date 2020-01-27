# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# Example:
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
        if (target - nums[i] in nums):
            pos = nums.index(target - nums[i])
            if pos!=i:
                result = [i,pos]
                return "Two index in nums are " + str(result)


print(twoSum([2,3,4], 7))

############
def twoSum(nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        print(buff_dict)
        for i in range(len(nums)):  # 0,1...4 len is 5
            if nums[i] in buff_dict:  # nums[0] = 1
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i   # dict[9-1] = dict[8] = 0 , dict [7] = 1 dic[6] = 2 dict[5] = 3
