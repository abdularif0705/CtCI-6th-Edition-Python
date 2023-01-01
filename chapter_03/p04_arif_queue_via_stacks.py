# 3.4 Queue Via Stacks

from chapter_03.stack import Stack


class MyQueue:
    def __init__(self):
        self.oldest_stack = Stack()
        self.newest_stack = Stack()

    def flip_onto_oldest_stack(self):  # flip the queue so that the oldest value is on top of the oldest stack
        if self.oldest_stack.is_empty():
            while not self.newest_stack.is_empty():
                self.oldest_stack.push(self.newest_stack.pop())  # now the Stack is flipped and the oldest item is on the top of the oldest_stack

    def enqueue(self, value):
        self.newest_stack.push(value)

    def dequeue(self):
        if self.oldest_stack.is_empty() == False:
            return self.oldest_stack.pop()
        else:
            self.flip_onto_oldest_stack()
            return self.oldest_stack.pop()

    def peek(self):
        if self.oldest_stack.is_empty() == False:
            return self.oldest_stack.peek()
        else:
            self.flip_onto_oldest_stack()
            return self.oldest_stack.peek()


class Tests:
    queue = MyQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
