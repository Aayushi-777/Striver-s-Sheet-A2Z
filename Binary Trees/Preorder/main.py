class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def preorder(self, root, arr):
        if root is None:
            return
        arr.append(root.data)
        self.preorder(root.left, arr)
        self.preorder(root.right, arr)
    def preorder_traversal(self, root):
        arr=[]
        self.preorder(root, arr)
        return arr
if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    result=sol.preorder_traversal(root)
    print("Preorder traversal:", *result)
    