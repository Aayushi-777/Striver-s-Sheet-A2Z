class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def length_of_loop(self, head):
        slow=fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return self.count_loop_length(slow)
        return 0
    def count_loop_length(self, meetpnt):
        temp=meetpnt
        length=1
        while temp.next!=meetpnt:
            temp=temp.next
            length+=1
        return length

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
    fifth.next=second
    length=sol.length_of_loop(head)
    print(f"The length of the loop in the linked list is: {length}")

    