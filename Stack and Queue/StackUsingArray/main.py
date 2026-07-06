class ArrayStack:
    def __init__(self, size=1000):
        self.stack=[0]*size
        self.top=-1
        self.size=size
    def push(self, x):
        if self.top<self.size-1:
            self.top+=1
            self.stack[self.top]=x
    def pop(self):
        if self.top==-1:
            return -1
        val=self.stack[self.top]
        self.top-=1
        return val
    def topElement(self):
        if self.top==-1:
            return -1
        return self.stack[self.top]
    def isEmpty(self):
        return self.top==-1

if __name__=="__main__":
    stack=ArrayStack()
    commands=["ArrayStack", "push", "push", "top", "pop", "isEmpty"]
    inputs=[[], [5], [10], [], [], []]
    for i in range(len(commands)):
        if commands[i]=="push":
            stack.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i]=="pop":
            print(stack.pop(), end=" ")
        elif commands[i]=="top":
            print(stack.topElement(), end=" ")
        elif commands[i]=="isEmpty":
            print("true" if stack.isEmpty() else "false", end=" ")
        elif commands[i]=="ArrayStack":
            print("null", end=" ")
        