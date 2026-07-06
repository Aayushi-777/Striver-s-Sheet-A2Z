class MinStack:
    def __init__(self):
        self.stack=[]
        self.minStack=[]
    def push(self, x):
        self.stack.append(x)
        if not self.minStack or x<=self.minStack[-1]:
            self.minStack.append(x)
    def pop(self):
        if not self.stack:
            return -1
        if self.stack[-1]==self.minStack[-1]:
            self.minStack.pop()
        return self.stack.pop()
    def top(self):
        if not self.stack:
            return -1
        return self.stack[-1]
    def getMin(self):
        if not self.minStack:
            return -1
        return self.minStack[-1]

if __name__=="__main__":
    ms=MinStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin(), end=" ")
    ms.pop()
    print(ms.top(), end=" ")
    ms.pop()
    print(ms.getMin())

