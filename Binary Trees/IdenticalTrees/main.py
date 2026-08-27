class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def is_identical(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return(root1.data==root2.data and self.is_identical(root1.left, root2.left) and self.is_identical(root1.right, root2.right))
if __name__=="__main__":
    sol=Solution()
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    ans=sol.is_identical(root1, root2)
    print(f"The trees are identical: {ans}")