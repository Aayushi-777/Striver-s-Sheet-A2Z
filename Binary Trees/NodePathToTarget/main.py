class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def find_path(self, root, arr, x):
        if root is None:
            return False
        arr.append(root.data)
        if root.data==x:
            return True
        if self.find_path(root.left, arr, x) or self.find_path(root.right, arr, x):
            return True
        arr.pop()
        return False
    def node_path(self, root, x):
        arr=[]
        if root is None:
            return arr
        self.find_path(root, arr, x)
        return arr
if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.left.left=Node(4)
    root.left.right=Node(10)
    root.left.left.right=Node(5)
    root.left.left.right.right=Node(6)
    root.right=Node(3)
    root.right.left=Node(9)
    root.right.right=Node(10)
    x=9
    ans=sol.node_path(root, x)
    print(ans)