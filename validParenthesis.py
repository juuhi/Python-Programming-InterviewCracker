class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        for brac in s:
            if brac in "([{":
                stack.append(brac)
            else:
                if not stack:
                    return False
                else:
                    top = stack[-1]
                    if brac == ')' and top == '(' or \
                       brac == ']' and top == '[' or \
                       brac == '}' and top == '{':
                        stack.pop()
                    else:
                      return False
        return len(stack) == 0

s1 = Solution()
print(s1.isValid("}"))

#####################################
# Simple way of writing the above program is ####
# The below program is using the stack 

class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        for brac in s:
            if brac in "([{":
                stack.append(brac)
 # and stack will check weather the stack is empty or not (if it is False, then before checking the third condition, 
 # it will return False, otherwise it will throw list out of index error)
            elif brac=="]" and stack and stack[-1]=="[":   
                stack.pop()
            elif brac=="}"  and stack and stack[-1]=="{":
                stack.pop()
            elif brac==")"  and stack and stack[-1]=="(":
                stack.pop()
            else:
                return False
        
        return len(stack)==0
