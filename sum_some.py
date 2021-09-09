Question :
  
>>>sum_some(0,100, [1,2,3,4,5])
0
>>>sum_some(0,100, [])
0
>>>sum_some(2,4, [1,2,3,4,5])
9

def sum_some(lower, upper, numbers):
    total = 0
    for num in numbers:
        if lower <= num <= upper:
            total += num
    return total
