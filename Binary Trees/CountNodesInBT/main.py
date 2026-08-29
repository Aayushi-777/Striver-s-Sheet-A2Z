class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def count_nodes(self, root):
        if not root:
            return 0
        left=self.left_height(root)
        right=self.right_height(root)
        if left==right:
            return (2**left)-1
        return 1+self.count_nodes(root.left)+self.count_nodes(root.right)
    def left_height(self, node):
        height=0
        while node:
            height+=1
            node=node.left
        return height
    def right_height(self, node):
        height=0
        while node:
            height+=1
            node=node.right
        return height
if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    ans=sol.count_nodes(root)
    print(ans)    