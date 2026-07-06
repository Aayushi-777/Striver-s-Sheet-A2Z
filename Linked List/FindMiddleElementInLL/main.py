#Tortoise and Hare Algorithm
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def middle_element(self, head):
        slow=fast=head
        while fast and fast.next and slow:
            fast=fast.next.next
            slow=slow.next
        return slow.data
    
if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    mid=sol.middle_element(head)
    print(f"The middle element is: {mid}")