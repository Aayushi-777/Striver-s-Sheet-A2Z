class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def left_dfs(self, node, level, res):
        if not node:
            return
        if len(res)==level:
            res.append(node.data)
        self.left_dfs(node.left, level+1, res)
        self.left_dfs(node.right, level+1, res)
    def right_dfs(self, node, level, res):
        if not node:
            return
        if len(res)==level:
            res.append(node.data)
        self.right_dfs(node.right, level+1, res)
        self.right_dfs(node.left, level+1, res)
    def left_view(self, root):
        res=[]
        self.left_dfs(root, 0, res)
        return res
    def right_view(self, root):
        res=[]
        self.right_dfs(root, 0, res)
        return res
if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.left.left=Node(4)
    root.left.right=Node(10)
    root.left.left.right=Node(5)
    root.left.left.right.right=Node(6)
    root.right=Node(3)
    root.right.left=Node(9)
    root.right.right=Node(10)
    r_view=sol.right_view(root)
    l_view=sol.left_view(root)
    print("Right view:", *r_view)
    print("Left view:", *l_view)