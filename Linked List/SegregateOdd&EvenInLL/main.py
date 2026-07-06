class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def segregate(self, head):
        if head is None or head.next is None:
            return head
        even_head=even_tail=None
        odd_head=odd_tail=None
        temp=head
        while temp:
            if temp.data%2==0:
                if not even_head:
                    even_head=even_tail=temp
                else:
                    even_tail.next=temp
                    even_tail=temp
            else:
                if not odd_head:
                    odd_head=odd_tail=temp
                else:
                    odd_tail.next=temp
                    odd_tail=temp
            temp=temp.next
        if not even_head:
            return odd_head
        if not odd_head:
            return even_head
        even_tail.next=odd_head
        odd_tail.next=None
        return even_head
    def print_list(self, head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    head = Node(17)
    head.next = Node(15)
    head.next.next = Node(8)
    head.next.next.next = Node(12)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(5)
    head.next.next.next.next.next.next = Node(4)
    new_head=sol.segregate(head)
    sol.print_list(new_head)
