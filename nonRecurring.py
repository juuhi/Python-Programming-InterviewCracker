# Print the first nonrecurring element in a list

#Examples:

#Input : -1 2 -1 3 2
#Output : 3
#Explanation : The first number that does not 
#repeat is : 3

#Input : 9 4 9 6 7 4
#Output : 6 */

from collections import defaultdict

def nonRecurring(arr):
    # initiate a hash table
    ht = defaultdict(lambda: 0)

    # insert all the elements of the array to the hashtable
    for i in range(len(arr)):
        ht[arr[i]] += 1

    # Traverse array to check the element with count 1
    for i in range(len(arr)):
        if ht[arr[i]] == 1:
            return arr[i]
    return "There is no non-recurring element"

# Driver code
#arr = [9,1,9,3,1,3]
arr = [1,2,2]
print(nonRecurring(arr))
