# Code from YoutTube video "Three In One: How to Implement 3 Stacks Using 1 Array | Microsoft Interview"
class ThreeStack:
    def __init__(self, capacity=2):
        capacity *= 3
        # items array populated with None values
        self.items = [None] * capacity
        # start array saves the position where each stack will start [0, 2, 4]
        self.start = [0, capacity // 3, 2 * (capacity // 3)]
        # end array saves the position where each stack will end [2, 4, 6]
        self.end = [capacity // 3, 2 * (capacity // 3), 3 * (capacity // 3)]

    def push(self, stack, val):
        # only stack 0, 1, and 2 exist
        if stack > 2:
            raise ValueError(f"Stack {stack} does NOT exist!")
        if self.start[stack] >= self.end[stack]:
            raise ValueError(f"Stack {stack} is FULL!")
        # items stores val at the starting position of that stack
        self.items[self.start[stack]] = val
        # increment the start position of the stack
        self.start[stack] += 1

    def pop(self, stack):
        if stack > 2:
            raise ValueError(f"Stack {stack} does NOT exist!")
        top = self.start[stack] - 1
        if top < 0 or self.items[top] == None:
            raise ValueError(f"Stack {stack} is EMPTY! Can't POP!")
        item = self.items[top]
        self.items[top] = None
        self.start[stack] = top
        return item

    # Same code as pop() except we just look at the value on the top of the stack
    def peek(self, stack):
        if stack > 2:
            raise ValueError(f"Stack {stack} does NOT exist!")
        top = self.start[stack] - 1
        if top < 0 or self.items[top] == None:
            raise ValueError(f"Stack {stack} is EMPTY! Can't POP!")
        return self.items[top]

    def display(self):
        print(self.items)


# Driver Code
a = ThreeStack()
a.push(1, 'C')
a.push(1, 'D')
# a.push(1,'E') # cause error cuz stack 1 is full
a.display()
print('pop stack #1:', a.pop(1))
a.display()
print('peek stack #1:', a.peek(1))
# print(a.peek(0)) # stack is Empty can't peek
