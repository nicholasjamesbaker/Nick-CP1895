# A simple class stack that only allows pop and push operations
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def clear(self):
        self.stack.clear()

    def length(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)


# And a queue that only has enqueue and dequeue operations
class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.queue:
            return self.queue[-1]
        else:
            return None

    def length(self):
        return len(self.queue)

    def __str__(self):
        return str(self.queue)


def main():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    print("STACK:", stack)
    print("PEEK:", stack.peek())
    print("LENGTH:", stack.length())
    print("IS EMPTY:", stack.is_empty())
    stack.clear()
    print("IS EMPTY:", stack.is_empty())
    print()

    queue = Queue()

    queue.enqueue(5)
    queue.enqueue(33)
    queue.enqueue(65)
    queue.dequeue()
    print("QUEUE:", queue)
    print("PEEK:", queue.peek())
    print("LENGTH:", queue.length())


if __name__ == "__main__":
    main()
