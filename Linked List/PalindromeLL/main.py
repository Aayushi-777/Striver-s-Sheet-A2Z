class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def reverse(self, head):
        if not head or not head.next:
            return head
        new_head=self.reverse(head.next)
        head.next.next=head
        head.next=None
        return new_head
    def is_palindrome(self, head):
        if not head or not head.next:
            return True
        slow=fast=head
        while fast.next is not None and fast.next.next is not None:
            slow=slow.next
            fast=fast.next.next
        new_head=self.reverse(slow.next)
        first=head
        second=new_head
        while second is not None:
            if first.data!=second.data:
                self.reverse(new_head)
                return False
            first=first.next
            second=second.next
        self.reverse(new_head)
        return True
    
if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(5)
    head.next.next=Node(2)
    head.next.next.next=Node(5)
    head.next.next.next.next=Node(1)
    ans=sol.is_palindrome(head)
    print(f"Is the linked list palindrome?: {ans}")
        