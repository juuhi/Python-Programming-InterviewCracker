#list1 = ['f', 'o', 'o']
#list2 = ['hello', 'world']

# desired output
#['f', 'hello', 'o', 'world', 'o']

# def countList(lst1, lst2):
#     # for sub in [lst1, lst2]:
#     #     return sub
#     return [sub[item] for item in range(len(lst2)) for sub in [lst1, lst2]]
#
# lst1 = [1, 2, 3]
# lst2 = ['a', 'b', 'c', None, None]
# print(countList(lst1, lst2))

# The above code fails if we have two lists of different length, we will get the out of bound length exception


def combine(list1, list2):
    lst = []
    len1 = len(list1)
    len2 = len(list2)

    for index in range( max(len1, len2) ):
        if index+1 <= len1:
            lst += [list1[index]]

        if index+1 <= len2:
            lst += [list2[index]]

    return lst

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c', None, None]
print(combine(lst1, lst2))
