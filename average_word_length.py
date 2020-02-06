# this program will calculate the average word length
# for the below list 
# [4,2,3,4] = 4+2+3+4 = 13/4 = 3

def avg(string):
    words = string.split(" ")
    average = sum(len(word) for word in words)//len(words)
    return average
    
    
    # can be done using the map function sum(map(func,list))
    # return sum(map(len, words))//len(words)

print(avg("This is the anna"))
