class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def postorder(self, root, arr):
        if root is None:
            return
        self.postorder(root.left, arr)
        self.postorder(root.right, arr)
        arr.append(root.data)
    def postorder_traversal(self, root):
        arr=[]
        self.postorder(root, arr)
        return arr
if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    result=sol.postorder_traversal(root)
    print("Postorder traversal: ", *result)