class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def inorder(self, root, arr):
        if root is None:
            return
        self.inorder(root.left, arr)
        arr.append(root.data)
        self.inorder(root.right, arr)
    def inorder_traversal(self, root):
        arr=[]
        self.inorder(root, arr)
        return arr
if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    result=sol.inorder_traversal(root)
    print("Inorder traversal: ", *result)