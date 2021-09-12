You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
Example 2:

Input: nums = [], lower = 1, upper = 1
Output: ["1"]
Explanation: The only missing range is [1,1], which becomes "1".
Example 3:

Input: nums = [], lower = -3, upper = -1
Output: ["-3->-1"]
Explanation: The only missing range is [-3,-1], which becomes "-3->-1".
  
  
  
###################################### Solution #########################################

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower-1] + nums + [upper+1]
        res = []
        
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                res.append(str(nums[i]+1))
            elif nums[i+1] - nums[i] > 2:
                res.append(str(nums[i]+1)+'->'+str(nums[i+1]-1))
        
        return res
      
#################below is the explanation and trying to solve the problem ##############################


 # if the difference is 2, then just append the lower + 1
# else append lower+1 -> upper - 1 (all converted to string)
    
#     [0,1,3,50,75]
#     i = 0 , 4
#     nums[3]-nums[2] == 2
#     nums[3]-nums[2] > 2 
    
#     [0,1,"2",3, "4 -> 49"]
