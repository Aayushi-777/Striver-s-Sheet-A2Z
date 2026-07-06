class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class QueueLL:
    def __init__(self):
        self.head=None
        self.end=None
    def push(self, x):
        new_node=Node(x)
        if self.head is None:
            self.head=self.end=new_node
        else:
            self.end.next=new_node
            self.end=new_node
    def pop(self):
        if self.head is None:
            return -1
        value=self.head.data
        self.head=self.head.next
        if self.head is None:
            self.end=None
        return value
    def peek(self):
        if self.head is None:
            return -1
        return self.head.data
    def isEmpty(self):
        return self.head is None

if __name__=="__main__":
    queue=QueueLL()
    commands=["LinkedListQueue", "push", "push", "peek", "pop", "isEmpty"]
    inputs=[[], [3], [7], [], [], []]
    for i in range(len(commands)):
        if commands[i] == "push":
            queue.push(inputs[i][0])
            print("null", end=" ")
        elif commands[i] == "pop":
            print(queue.pop(), end=" ")
        elif commands[i] == "peek":
            print(queue.peek(), end=" ")
        elif commands[i] == "isEmpty":
            print("true" if queue.isEmpty() else "false", end=" ")
        elif commands[i] == "LinkedListQueue":
            print("null", end=" ")