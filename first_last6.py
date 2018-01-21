def first_last6(nums):
  return len(nums)> 1 and (nums[0]==6 or nums[-1]==6)

print first_last6([1,2,6])
print first_last6([6,1,1])
print first_last6([6,1,6])
print first_last6([1,1,1])