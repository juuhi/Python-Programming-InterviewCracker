# Return the number of times that the string "code" appears anywhere in the given string,
# except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb')
# count_code('codexxcode')
# count_code('cozexxcope')

def count_code(str):
    count=0
    for i in range(len(str)-3):
        if str[i:i+2]+str[i+3]=="coe":
            count = count+1
    return count

print count_code('aaacodebbb')
print count_code('codexxcode')
print count_code('cozexxcope')