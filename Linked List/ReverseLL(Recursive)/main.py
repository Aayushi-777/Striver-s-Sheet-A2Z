class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def reverse_list(self, head):
        if head is None or head.next is None:
            return head
        new_head=self.reverse_list(head.next)
        front=head.next
        front.next=head
        head.next=None
        return new_head

if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    new_head=sol.reverse_list(head)
    while new_head:
        print(new_head.data, end=" ")
        new_head=new_head.next
    print()