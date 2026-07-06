from queue import Queue
class QueueStack:
    def __init__(self):
        self.q=Queue()
    def push(self, x):
        s=self.q.qsize()
        self.q.put(x)
        for _ in range(s):
            self.q.put(self.q.get())
    def pop(self):
        if self.q.empty():
            return -1
        return self.q.get()
    def top(self):
        if self.q.empty():
            return -1
        return self.q.queue[0]
    def isEmpty(self):
        return self.q.empty()

if __name__=="__main__":
    stack=QueueStack()
    commands=["QueueStack", "push", "push", "pop", "top", "isEmpty"]
    inputs=[[], [4], [8], [], [], []]
    for i in range(len(commands)):
        if commands[i] == "QueueStack":
            print("null", end=" ")
        elif commands[i] == "push":
            stack.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(stack.pop(), end=" ")
        elif commands[i] == "top":
            print(stack.top(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if stack.isEmpty() else "false", end=" ")