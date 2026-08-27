class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def max_path_sum(self, root):
        self.max_sum=float('-inf')
        def dfs(node):
            if node is None:
                return 0
            left=max(0, dfs(node.left))
            right=max(0, dfs(node.right))
            self.max_sum=max(self.max_sum, left+right+node.data)
            return max(left, right)+node.data
        dfs(root)
        return self.max_sum
if __name__=="__main__":
    sol=Solution()
    root=Node(-10)
    root.left=Node(9)
    root.right=Node(20)
    root.right.left=Node(15)
    root.right.right=Node(7)
    ans=sol.max_path_sum(root)
    print(ans)