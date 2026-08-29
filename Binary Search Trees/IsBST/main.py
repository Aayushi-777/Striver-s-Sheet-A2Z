class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def is_bst(self, root):
        def check(node, low, high):
            if not node:
                return True
            if node.data<=low or node.data>=high:
                return False
            return check(node.left, low, node.data) and check(node.right, node.data, high)
        return check(root, float('-inf'), float('inf'))
if __name__=="__main__":
    sol=Solution()
    root=Node(5)
    root.left=Node(3)
    root.right=Node(6)
    root.left.left=Node(2)
    root.left.right=Node(4)
    root.right.right=Node(7)
    ans=sol.is_bst(root)
    print(f"The tree is a binary search tree: {ans}")