class ArrayQueue:
    def __init__(self, size=100):
        self.queue=[0]*size
        self.size=size
        self.front=-1
        self.rear=-1
        self.count=0
    def push(self, x):
        if self.count==self.size:
            return
        if self.front==-1:
            self.front=self.rear=0
        else:
            self.rear=(self.rear+1)%self.size
        self.queue[self.rear]=x
        self.count+=1
    def pop(self):
        if self.count==0:
            return -1
        val=self.queue[self.front]
        if self.count==1:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        self.count-=1
        return val
    def peek(self):
        if self.count==0:
            return -1
        return self.queue[self.front]
    def isEmpty(self):
        return self.count==0

if __name__=="__main__":
    queue=ArrayQueue()
    commands=["ArrayQueue", "push", "push", "peek", "pop", "isEmpty"]
    inputs=[[], [5], [10], [], [], []]
    for i in range(len(commands)):
        if commands[i]=="push":
            queue.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i]=="pop":
            print(queue.pop(), end=" ")
        elif commands[i]=="peek":
            print(queue.peek(), end=" ")
        elif commands[i]=="isEmpty":
            print("true" if queue.isEmpty() else "false", end=" ")
        elif commands[i]=="ArrayQueue":
            print("null", end=" ")