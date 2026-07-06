class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def detect_loop(self, head):
        temp=head
        node_map={}
        while temp is not None:
            if temp in node_map:
                return True
            node_map[temp]=1
            temp=temp.next
        return False

if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    second=Node(2)
    third=Node(3)
    fourth=Node(4)
    fifth=Node(5)
    head.next=second
    second.next=third
    third.next=fourth
    fourth.next=fifth
    fifth.next=third
    ans=sol.detect_loop(head)
    print(f"Is there a loop in the linked list?: {ans}")
    