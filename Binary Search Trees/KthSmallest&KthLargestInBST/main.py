class Node:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def kth_smallest(self, root, k):
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            k-=1
            if k==0:
                return root.data
            root=root.right
    def kth_largest(self, root, k):
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.right
            root=stack.pop()
            k-=1
            if k==0:
                return root.data
            root=root.left
if __name__=="__main__":
    sol=Solution()
    root=Node(3)
    root.left=Node(1)
    root.left.right=Node(2)
    root.right=Node(4)
    k=1
    small=sol.kth_smallest(root, k)
    large=sol.kth_largest(root, k)
    print(f"Kth largest node: {large}")
    print(f"Kth smallest node: {small}")