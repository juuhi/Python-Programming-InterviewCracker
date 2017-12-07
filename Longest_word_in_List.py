# Find the length of the longest word in a list
# Want to know the input from the user as a list and then processing

def find_longest_word(myList):
    return max(len(i) for i in myList)

myList = ['a','bbb','cccc']
print('The length of the longest word is ' +str(find_longest_word(myList)))

