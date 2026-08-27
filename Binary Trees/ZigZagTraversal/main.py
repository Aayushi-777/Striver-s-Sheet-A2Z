from collections import deque
class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def zig_zag_traversal(self, root):
        res=[]
        if not root:
            return res
        q=deque([root])
        left_to_right=True
        while q:
            size=len(q)
            level=[0]*size
            for i in range(size):
                node=q.popleft()
                index=i if left_to_right else size-1-i
                level[index]=node.data
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            left_to_right=not left_to_right
            res.append(level)
        return res
if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.right=Node(6)
    ans=sol.zig_zag_traversal(root)
    print(ans)