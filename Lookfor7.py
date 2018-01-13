# #[2,3,4,5,6,13,12,7,2] -> 16
#
# def skip67(nums):
#     total = 0
#     i = 0
#     flag = True
#     while i<len(nums):
#         if nums[i] == 6:
#             while nums[i]!=7:
#                 i=i+1
#             i=i+1
#         else:
#             total = total+nums[i]
#             i=i+1
#     return total
#
# print skip67([2,3,4,5,6,13,12,7,2])
# print skip67([1, 2, 2])
# print skip67([1, 2, 2, 6, 99, 99, 7])
# print skip67([1, 1, 6, 7, 2])
#         #     flag = False
#         #     i = i+1
#         #     if flag =
#         # else:
#         #     total=total+nums[i]

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
