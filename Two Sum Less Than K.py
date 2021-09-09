Given an array nums of integers and integer k, return the maximum sum such that there exists i < j with nums[i] + nums[j] = sum and sum < k. If no i, j exist satisfying this equation, return -1.

 

Example 1:

Input: nums = [34,23,1,24,75,33,54,8], k = 60
Output: 58
Explanation: We can use 34 and 24 to sum 58 which is less than 60.
Example 2:

Input: nums = [10,20,30], k = 15
Output: -1
Explanation: In this case it is not possible to get a pair sum less that 15.
  
  
###################################

def towSumLessThanK(A,K): 
		a = sorted(A) 
		i,j = 0,len(a)-1
        ans = -1
        while i<j:
            if a[i]+a[j]<K:
                ans = max(ans,a[i]+a[j])
                i += 1
            else:
                j -= 1
        return ans
      
 The complexity is O(nlogn) [for sorting the list] + O(n) [for searching the combination]

yes, but because O(nlogn) is prevalent compared to O(n), final time complexity is O(nlogn)
