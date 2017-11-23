#Define a function max() that takes two numbers as arguments and returns the largest of
# them. Use the if-then- else construct available in Python.

def max(a,b):
    if a >b:
        return a
    else:
        return b
print('Enter the first number')   # Input from the user
aA = input()
print('Enter the second number')
bB = input()

print (str(max(aA,bB) + ' is larger number'))