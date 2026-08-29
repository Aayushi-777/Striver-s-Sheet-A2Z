class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def predecessor(self, root, p):
        predecessor=None
        while root:
            if p.data>root.data:
                predecessor=root
                root=root.right
            else:
                root=root.left
        return predecessor.data
    def successor(self, root, p):
        successor=None
        while root:
            if p.data<root.data:
                successor=root
                root=root.left
            else:
                root=root.right
        return successor.data
if __name__=="__main__":
    sol=Solution()
    root = Node(5)
    root.left = Node(3)
    root.right = Node(6)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right.right = Node(7)
    p=root.left.right
    succ=sol.successor(root, p)
    pred=sol.predecessor(root, p)
    print(f"Predecessor: {pred}")
    print(f"Successor: {succ}")