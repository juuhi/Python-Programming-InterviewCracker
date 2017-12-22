"""juhiNewYork"""

def count_words(string):
    total = 1
    for i in string:
        if i.isupper():
            total += 1
    return total

print(count_words('juhiSharmaIndia'))