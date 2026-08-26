class Node:
    def __init__(self, data):
        self.data=data
        self.right=None
        self.left=None
class Solution:
    def preInPostTraversal(self, root):
        pre, ino, post=[], [], []
        if root is None:
            return []
        st=[(root, 1)]
        while st:
            node, state=st.pop()
            if state==1:
                pre.append(node.data)
                st.append((node, 2))
                if node.left:
                    st.append((node.left, 1))
            elif state==2:
                ino.append(node.data)
                st.append((node, 3))
                if node.right:
                    st.append((node.right, 1))
            else:
                post.append(node.data)
        return [pre, ino, post]

if __name__=="__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    sol=Solution()
    traversals=sol.preInPostTraversal(root)
    pre=traversals[0]
    ino=traversals[1]
    post=traversals[2]
    print("Preorder traversal:", *pre)
    print("Inorder traversal:", *ino)
    print("Postorder traversal:", *post)

