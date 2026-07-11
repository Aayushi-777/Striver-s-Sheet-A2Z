class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.child=None
class Solution:
    def merge(self, l1, l2):
        dummy=Node(-1)
        temp=dummy
        while l1 and l2:
            if l1.data<l2.data:
                temp.child=l1
                temp=l1
                l1=l1.child
            else:
                temp.child=l2
                temp=l2
                l2=l2.child
            temp.next=None
        if l1:
            temp.child=l1
        else:
            temp.child=l2
        return dummy.child
    def flatten_ll(self, head):
        if head is None or head.next is None:
            return head
        merge_head=self.flatten_ll(head.next)
        return self.merge(head, merge_head)
    def print_ll(self, head):
        while head:
            print(head.data, end=" ")
            head=head.child
        print()
    def print_original_ll(self, head, depth=0):
        while head:
            print(head.data, end=" ")
            if head.child:
                print("-> ", end="")
                self.print_original_ll(head.child, depth+1)
            if head.next:
                print()
                print("| "*depth, end="")
            head=head.next

if __name__=="__main__":
    sol=Solution()
    head = Node(5)
    head.child = Node(14)
    head.next = Node(10)
    head.next.child = Node(4)
    head.next.next = Node(12)
    head.next.next.child = Node(20)
    head.next.next.child.child = Node(13)
    head.next.next.next = Node(7)
    head.next.next.next.child = Node(17)
    print("Original Linked List:")
    sol.print_original_ll(head)
    flattened=sol.flatten_ll(head)
    print("\nFlattened Linked List:")
    sol.print_ll(flattened)