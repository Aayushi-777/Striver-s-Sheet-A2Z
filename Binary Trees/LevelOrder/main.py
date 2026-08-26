from collections import deque
class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def level_order(self, root):
        ans=[]
        if not root:
            return ans
        q=deque([root])
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level)
        return ans
if __name__=="__main__":
    sol=Solution()
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    result=sol.level_order(root)
    print(*result)
