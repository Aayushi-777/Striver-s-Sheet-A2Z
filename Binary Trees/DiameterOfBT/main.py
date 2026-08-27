class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def diameter(self, root):
        ans=[0]
        def height(node):
            if node is None:
                return 0
            left=height(node.left)
            right=height(node.right)
            ans[0]=max(ans[0], left+right)
            return max(left, right)+1
        height(root)
        return ans[0]
if __name__=="__main__":
    sol=Solution()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.right.right = Node(6)
    root.left.right.right.right = Node(7)
    ans=sol.diameter(root)
    print(ans)