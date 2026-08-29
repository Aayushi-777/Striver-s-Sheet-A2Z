class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def insert_node(self, root, val):
        if root is None:
            return Node(val)
        if val<root.data:
            root.left=self.insert_node(root.left, val)
        else:
            root.right=self.insert_node(root.right, val)
        return root
if __name__=="__main__":
    sol=Solution()
    root=Node(8)
    root.left=Node(4)
    root.right=Node(12)
    root.left.left=Node(2)
    root.left.right=Node(6)
    root.right.left=Node(10)
    root.right.right=Node(14)
    val=11
    root=sol.insert_node(root, val)
    print(root.data)