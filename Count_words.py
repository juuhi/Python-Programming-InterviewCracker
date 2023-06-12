"""juhiNewYork"""

def count_words(string):
    total = 0
    for i in string:
        if i.upper():
            total += 1
    return total

print(count_words('juhiSharmaIndia'))
