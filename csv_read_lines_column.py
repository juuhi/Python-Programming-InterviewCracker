# This program will print the first 5 records of 2nd and 4th column of the csv flat file (either in the same directory or in some other directory)
# when you copy the path it will come with the backslash, change that to the forward slash and second parameter will be mode to open the file

import csv
# with open('C:/Users/sharju7/PycharmProjects/test/test.csv', "rt") as f:
with open('C:/Users/sharju7/Desktop/test.csv', 'rt') as f:
    counter = 0
    for line in f:
        x = line.split(',')[1]
        y = line.split(',')[3]
        print(x,y)
        counter += 1
        if counter == 5:
            break
