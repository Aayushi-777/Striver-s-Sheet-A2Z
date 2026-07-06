class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def insert_node(self, head1, head2):
        p1=head1
        p2=head2
        while p1!=p2:
            p1=head2 if p1 is None else p1.next
            p2=head1 if p2 is None else p2.next
        return p1
    def print_ll(self, head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    head1=Node(1)
    head1.next=Node(3)
    head1.next.next=Node(1)
    head1.next.next.next=Node(2)
    head1.next.next.next.next=Node(4)
    head2=Node(3)
    head2.next=head1.next.next.next 
    print("List1:", sol.print_ll(head1))
    print("List2:", sol.print_ll(head2))
    ans=sol.insert_node(head1, head2)
    if ans:
        print(f"Intersection at: {ans.data}")
    else:
        print("No intersection")