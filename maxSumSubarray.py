 # Find consecutive elements in array which has maximum sum.
 
 # Largest Sum Contiguous Subarray
 
 def maxSum(arr):
    # [1,2,3,4,-1,4]
    cur_sum = 0
    max_sum = 0
    start = 0
    end = 0
    s = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        if cur_sum > max_sum:
            max_sum = cur_sum
            start = s
            end = i

        if cur_sum < 0:
            cur_sum = 0
            s = i+1

    print("Starting index is %d" %(start))
    print("Ending index is %d" %(end))
    print("Maximum sum Subarray is " + str(arr[start:end+1]))
    return max_sum

#arr = [1,2,3,4,-1,4]
#arr = [1,2,3,4,-1,4, -14]
# test case are :
arr = [1,2,3,4,-1,4,-14, 144, 0]
print(maxSum(arr))
