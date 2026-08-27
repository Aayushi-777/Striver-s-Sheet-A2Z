class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def is_symmetric(self, root):
        if root is None:
            return True
        def mirror(left, right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (left.data==right.data and mirror(left.left, right.right) and mirror(left.right, right.left))
        return mirror(root.left, root.right)
if __name__=="__main__":
    sol=Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(2)
    root.left.left = Node(3)
    root.left.right = Node(4)
    root.right.left = Node(4)
    root.right.right = Node(3)
    ans=sol.is_symmetric(root)
    print(f"The binary tree is symmetric: {ans}")
    