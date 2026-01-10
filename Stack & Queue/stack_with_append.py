class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)     # Add item to top of stack using append
        print(f"Pushed: {item}")

    def peek(self):
        if not self.is_empty():                   # Return top item without removing it
            return self.items[-1]            # last element using - index
        return None

    def pop(self):
        if not self.is_empty():                  # Remove and return top item
            return self.items.pop()
        return None

    def is_empty(self):  # Check if stack is empty
        return len(self.items) == 0


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)
print(stack.peek())
