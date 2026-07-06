class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class StackLL:
    def __init__(self):
        self.head=None
    def push(self, x):
        new_node=Node(x)
        new_node.next=self.head
        self.head=new_node
    def pop(self):
        if self.head is None:
            return -1
        value=self.head.data
        self.head=self.head.next
        return value
    def top(self):
        if self.head is None:
            return -1
        return self.head.data
    def isEmpty(self):
        return self.head is None

if __name__=="__main__":
    stack=StackLL()
    commands=["LinkedListStack", "push", "push", "pop", "top", "isEmpty"]
    input=[[], [3], [7], [], [], []]
    for i in range(len(commands)):
        if commands[i]=="push":
            stack.push(input[i][0])
            print("null", end=" ")
        elif commands[i]=="pop":
            print(stack.pop(), end=" ")
        elif commands[i]=="top":
            print(stack.top(), end=" ")
        elif commands[i]=="isEmpty":
            print(stack.isEmpty(), end=" ")
        elif commands[i]=="LinkedListStack":
            print("null", end=" ")
        