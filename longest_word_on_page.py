# This program will  print the largest element of a page and then the size of the element
# I am stripping for the leading and trailing spaces and also using regex to eliminate the special characters
# You can remove the sub condition if you want the character as alphanumeric

import re
def longest_word(string):
    cur_elem = " "
    s = re.sub("[^0-9a-zA-Z']+",' ',string).strip()
    new_list = s.split(" ")
    print(new_list)
    for i in range(0,len(new_list)):
        if len(cur_elem) < len(new_list[i]):
            cur_elem = new_list[i]
    return cur_elem, len(cur_elem)

string = "     This is the phe@nonmenon of saying that hard work always pays off and perseverance always matter to   be  " \
         "successfull in life    "
print(longest_word(string))

# Note : Strip can't be performed on list
#append can't be performed on string
