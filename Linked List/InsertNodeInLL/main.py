class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class Solution:
    def insert_at_beginning(self, head, val):
        new_node=Node(val)
        new_node.next=head
        return new_node
    def print_list(self, head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    head=Node(2)
    head.next=Node(3)
    sol.print_list(head)
    head=sol.insert_at_beginning(head, 1)
    print("After insertion at head:", end=" ")
    sol.print_list(head)