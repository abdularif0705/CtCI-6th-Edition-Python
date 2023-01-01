# From neetcode's gh, i added my own Driver Code at the bottom though and tweaked a few things
class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)  # push value onto the reg stack
        print('pushed =', val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

    def display(self):
        print(self.stack)


stack = MinStack()
stack.push(5)
stack.push(6)
stack.display()
print('minimum =', stack.getMin())
print('pop = ', stack.pop())
stack.push(2)
stack.display()
print('minimum =', stack.getMin())
stack.push(-2)
stack.display()
print('minimum =', stack.getMin())
# stack.display()
