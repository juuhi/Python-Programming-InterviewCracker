def insertionSort(arr):
    is_sorted = False
    value = arr[-1]
    i = 2

    while i <= len(arr):
        if arr[-i] > value:
            arr[-i + 1] = arr[-i]
            print(array_to_string(arr))
        elif arr[-i] < value:
            arr[-i + 1] = value
            print(array_to_string(arr))
            is_sorted = True
            break
        i += 1

    if not is_sorted:
        if arr[0] > value:
            arr[1] = arr[0]
            arr[0] = value
        print(array_to_string(arr))

    return arr


def array_to_string(arr):
    temp_list = []
    for var in arr:
        temp_list.append(str(var))
    return ' '.join(temp_list)


m = int(input())
ar = [int(i) for i in input().strip().split()]
insertionSort(ar)

