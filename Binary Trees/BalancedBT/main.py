class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def is_balanced(self, root):
        return self.height(root)!=-1
    def height(self, root):
        if root is None:
            return 0
        left=self.height(root.left)
        if left==-1:
            return -1
        right=self.height(root.right)
        if right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return max(left, right)+1
if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.left.right.right=Node(6)
    root.left.right.right.right=Node(7)
    res=sol.is_balanced(root)
    print(f"The binary tree is balanced?: {res}")