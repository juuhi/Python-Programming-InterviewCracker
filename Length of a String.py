# Define a function that computes the length of a given list or string. (It is true that Python
# has the len() function built in, but writing it yourself is nevertheless a good exercise.)

def countLength(string):
    count = 0
    for i in string:
        count += 1
    return count    # return is the best way as we do not need to intialize another variable that occupy memory

print('Enter a String')
string = input()

print('Length of the String is ' + str(countLength(string))) #function calling (print by converting number into string)