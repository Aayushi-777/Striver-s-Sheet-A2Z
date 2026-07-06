class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

if __name__=="__main__":
    arr=[2, 5, 8, 7]
    head=Node(arr[0])
    print(head.data)