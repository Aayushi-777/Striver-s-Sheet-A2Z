class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def print_ll(self, head):
        temp=head
        while temp is not None:
            print(temp.data, end=" ")
            temp=temp.next
        print()
    def delete_node(self, head, N):
        dummy=Node(0)
        dummy.next=head
        slow=fast=dummy
        for _ in range(N+1):
            fast=fast.next
        while fast is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return dummy.next

if __name__=="__main__":
    sol=Solution()
    N=3
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    head=sol.delete_node(head, N)
    sol.print_ll(head)
