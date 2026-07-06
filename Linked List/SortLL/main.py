class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def merge_ll(self, l1, l2):
        dummy=Node(-1)
        temp=dummy
        while l1 and l2:
            if l1.data<=l2.data:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
        if l1:
            temp.next=l1
        else:
            temp.next=l2
        return dummy.next
    def middle(self, head):
        if not head or not head.next:
            return head
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def sort_ll(self, head):
        if not head or not head.next:
            return head
        middle=self.middle(head)
        right=middle.next
        middle.next=None
        left=head
        left=self.sort_ll(left)
        right=self.sort_ll(right)
        return self.merge_ll(left, right)
    def print_ll(self, head):
        temp=head
        while temp is not None:
            print(temp.data, end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    head=Node(3)
    head.next=Node(2)
    head.next.next=Node(5)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(1)
    print("Orignal LL:", sol.print_ll(head))
    new_head=sol.sort_ll(head)
    print("Sorted LL:", sol.print_ll(new_head))