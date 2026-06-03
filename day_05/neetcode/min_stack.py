class MinStack:
    def __init__(self):
        self.stack =[]
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val )
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minStack[-1]
    


obj = MinStack()

obj.push(-2)
obj.push(0)
obj.push(-3)

assert obj.getMin() == -3, "Error: Minimum should be -3"
assert obj.top() == -3, "Error: Top element should be -3"

obj.pop()
assert obj.top() == 0, "Error: Top element should now be 0"
assert obj.getMin() == -2, "Error: Minimum should revert back to -2"

obj.push(-2)
assert obj.getMin() == -2, "Error: Minimum should still be -2"
assert obj.top() == -2, "Error: Top element should be -2"

obj.pop()
assert obj.getMin() == -2, "Error: Minimum should remain -2 after popping duplicate"

print("All assert tests passed successfully!")
