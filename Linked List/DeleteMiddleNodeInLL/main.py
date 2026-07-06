class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def delete_middle(self, head):
        if head is None or head.next is None:
            return None
        slow=head
        fast=head.next.next
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        slow.next=slow.next.next
        return head
    def print_ll(self, head):
        temp=head
        while temp is not None:
            print(temp.data, end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    print("Original LL:", sol.print_ll(head))
    new_head=sol.delete_middle(head)
    print("After deleting the middle node:", sol.print_ll(new_head))
