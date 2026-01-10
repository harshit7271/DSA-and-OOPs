class stack:
    def __init__(self):
        self.s = []   # s is a list

    def length(self):
        return len(self.s)

    def push(self, value):
        self.s.insert(0, value)
        print(f"Pushed : {value}")

    def peek(self):                              # to check what's there at the top of the stack
        if len(self.s) == 0:
            raise Exception("I AM SORRY BABU STACK IS EMPTY")
        else:
            return self.s[0]

    def pop(self):                                # to delete the element at the top
        if len(self.s) == 0:
            raise Exception("I AM SORRY BABU STACK IS EMPTY")
        else:
            return self.s.pop(0)


stk = stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)

print(stk.peek())
