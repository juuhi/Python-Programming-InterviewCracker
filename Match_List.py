# Given two list of srings, a and b, return the count of the matched strings.

def string_match(a,b):
    count = 0
    for i in range(min(len(a),len(b))):
        if a[i]==b[i]:
            count = count+1
    return count
print string_match(['a','b','c','d'], ['a','b','c'])
print string_match(['a','b'],['a'])
print string_match(['juhi','sharma'],['juhi','sharma','juhi'])
