class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def ceiling(self, root, x):
        ans=None
        while root:
            if root.data==x:
                return root.data
            if root.data>x:
                ans=root.data
                root=root.left
            else:
                root=root.right
        return ans
    def floor(self, root, x):
        ans=None
        while root:
            if root.data==x:
                return root.data
            if root.data<x:
                ans=root.data
                root=root.right
            else:
                root=root.left
        return ans
if __name__=="__main__":
    sol=Solution()
    root=Node(8)
    root.left=Node(4)
    root.right=Node(12)
    root.left.left=Node(2)
    root.left.right=Node(6)
    root.right.left=Node(10)
    root.right.right=Node(14)
    x=11
    floor=sol.floor(root, x)
    ceiling=sol.ceiling(root, x)
    print(f"Floor: {floor}")
    print(f"Ceiling: {ceiling}")