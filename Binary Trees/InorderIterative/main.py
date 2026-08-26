class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def inorder(self, root):
        inorder=[]
        stack=[]
        node=root
        while stack or node:
            while node:
                stack.append(node)
                node=node.left
            node=stack.pop()
            inorder.append(node.data)
            node=node.right
        return inorder
if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)          
    result=sol.inorder(root)
    print("Inorder traversal:", *result)