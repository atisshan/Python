class stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)
    
my_stack=stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)

print("Top of the stack", my_stack.peek())

popped_item=my_stack.pop()
if popped_item is not None:
    print("Popped item", popped_item())

print("Is the stack empty?", my_stack.is_empty())
print("Size of the stack:", my_stack.size())