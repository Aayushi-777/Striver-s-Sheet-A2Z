class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def is_leaf(self, root):
        return not root.left and not root.right
    def add_left_boundary(self, root, res):
        curr=root.left
        while curr:
            if not self.is_leaf(curr):
                res.append(curr.data)
            if curr.left:
                curr=curr.left
            else:
                curr=curr.right
    def add_right_boundary(self, root, res):
        curr=root.right
        temp=[]
        while curr:
            if not self.is_leaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr=curr.right
            else:
                curr=curr.left
        for i in range(len(temp)-1, -1, -1):
            res.append(temp[i])
    def add_leaves(self, root, res):
        if self.is_leaf(root):
            res.append(root.data)
            return
        if root.left:
            self.add_leaves(root.left, res)
        if root.right:
            self.add_leaves(root.right, res)
    def print_boundary(self, root):
        res=[]
        if not root:
            return res
        if not self.is_leaf(root):
            res.append(root.data)
        self.add_left_boundary(root, res)
        self.add_leaves(root, res)
        self.add_right_boundary(root, res)
        return res
if __name__=="__main__":
    sol=Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    res=sol.print_boundary(root)
    print(*res)
