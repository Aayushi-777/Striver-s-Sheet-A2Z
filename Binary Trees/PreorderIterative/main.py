class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def preorder(self, root):
        preorder=[]
        if root is None:
            return preorder
        stack=[root]
        while stack:
            node=stack.pop()
            preorder.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    result=sol.preorder(root)
    print("Preorder traversal:", *result)