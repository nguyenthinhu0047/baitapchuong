class Stack:
    def __init__(self, max_size=10):
        self.stack = []
        self.max_size = max_size

    def push(self, item):
        if not self.isFull():
            self.stack.append(item)
        else:
            print("Stack is full!")

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            print("Stack is empty!")
            return None

    def isEmpty(self):
        return len(self.stack) == 0

    def isFull(self):
        return len(self.stack) == self.max_size
s = Stack(5)
s.push(1.1)
s.push(2.2)
s.push(3.3)
print(s.pop())  
print(s.isEmpty()) 
print(s.isFull())  