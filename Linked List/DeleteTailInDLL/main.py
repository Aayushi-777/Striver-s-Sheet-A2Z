class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
class Solution:
    def delete_tail(self, head):
        if not head or not head.next:
            return None
        temp=head
        while temp.next:
            temp=temp.next
        temp.prev.next=None
        return head

if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.prev=head
    head.next.next=Node(3)
    head.next.next.prev=head.next
    head=sol.delete_tail(head)
    temp=head
    while temp:
        print(temp.data, end=" ")
        temp=temp.next
    print()

        