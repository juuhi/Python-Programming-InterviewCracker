# create the stack operations using list
class Stack():
    def __init__(self):
        self.items = []   # constructor will going to modify the python list

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()  # pop operation also exist in the list, remove will eliminate all the elements from the list at once.

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def getMin(self):
        return min(self.items)

s = Stack()
s.push("A")
s.push("B")
print(s.get_stack())
s.push("C")
s.push(1)
s.push("Create a new file")
s.push("D")
s.pop()
print(s.get_stack())
print(s.is_empty())
print(s.peek())
