def findDuplicate(list):
    list1 = set(list)
    # list = [1,2,3,2]
    # list1 = [1,2,3]
    y = [x for x in list if list.count(x) > 1]
    return y

print(findDuplicate([1,2,3,4,2]))
