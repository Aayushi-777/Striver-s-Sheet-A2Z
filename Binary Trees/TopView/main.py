from collections import deque
class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def top_view(self, root):
        if not root:
            return []
        q=deque([(root, 0)])
        top={}
        while q:
            node, hd=q.popleft()
            if hd not in top:
                top[hd]=node.data
            if node.left:
                q.append((node.left, hd-1))
            if node.right:
                q.append((node.right, hd+1))
        return [top[x] for x in sorted(top)]
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
    ans=sol.top_view(root)
    print(*ans)    