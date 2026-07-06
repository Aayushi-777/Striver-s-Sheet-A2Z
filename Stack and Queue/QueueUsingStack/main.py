class StackQueue:
    def __init__(self):
        self.input=[]
        self.output=[]
    def push(self, x):
        self.input.append(x)
    def pop(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            return -1
        return self.output.pop()
    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        if not self.output:
            return -1
        return self.output[-1]
    def isEmpty(self):
        return not self.output and not self.input

if __name__=="__main__":
    queue=StackQueue()
    queue.push(3)
    queue.push(4)
    print("The element popped is", queue.pop())
    queue.push(5)
    print("The front of the queue is", queue.peek())
    print("Is the queue empty?", "Yes" if queue.isEmpty() else "No")
