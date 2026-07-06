class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

if __name__=="__main__":
    arr=[2, 5, 8, 7]
    y=Node(arr[0])
    print(y)
    print(y.data)