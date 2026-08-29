class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def binary_search_tree(self, root, target):
        while root and root.data!=target:
            if target<root.data:
                root=root.left
            else:
                root=root.right
        return root

if __name__=="__main__":
    sol=Solution()
    root=Node(4)
    root.left=Node(2)
    root.right=Node(7)
    root.left.left=Node(1)
    root.left.right=Node(3)
    target=7
    res=sol.binary_search_tree(root, target)
    if res:
        print(f"Node found: {res.data}")
    else:
        print("Node not there in the binary tree")
