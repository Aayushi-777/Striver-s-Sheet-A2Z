from collections import deque, defaultdict
class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def find_vertical(self, root):
        if not root:
            return []
        nodes=defaultdict(lambda: defaultdict(list))
        queue=deque([(root, 0, 0)])
        while queue:
            node, x, y=queue.popleft()
            nodes[x][y].append(node.data)
            if node.left:
                queue.append((node.left, x-1, y+1))
            if node.right:
                queue.append((node.right, x+1, y+1))
        result=[]
        for x in sorted(nodes):
            column=[]
            for y in sorted(nodes[x]):
                column.extend(sorted(nodes[x][y]))
            result.append(column)
        return result
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
    ans=sol.find_vertical(root)
    print(*ans)