class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def rotate_right(self, head, k):
        if not head or not head.next or k==0:
            return head
        length=1
        tail=head
        while tail.next:
            tail=tail.next
            length+=1
        tail.next=head
        k=k%length
        steps_to_new_tail=length-k
        new_tail=head
        for _ in range(1, steps_to_new_tail):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None
        return new_head
    
if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    k=2
    new_head=sol.rotate_right(head, k)
    while new_head:
        print(new_head.data, end=" ")
        new_head=new_head.next
        