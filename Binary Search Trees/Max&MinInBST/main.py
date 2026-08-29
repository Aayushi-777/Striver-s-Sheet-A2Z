class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def find_min(self, root):
        if root is None:
            return None
        while root.left:
            root=root.left
        return root.data
    def find_max(self, root):
        if root is None:
            return None
        while root.right:
            root=root.right
        return root.data
if __name__=="__main__":
    sol=Solution()
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)
    mini=sol.find_min(root)
    maxi=sol.find_max(root)
    print(f"Minimum value: {mini}")
    print(f"Maximum value: {maxi}")