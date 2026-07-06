class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
class Solution:
    def convert_to_dll(self, arr):
        head=Node(arr[0])
        prev=head
        for val in arr[1:]:
            node=Node(val)
            prev.next=node
            node.prev=prev
            prev=node
        return head
    def print_dll(self, head):
        while head:
            print(head.data, end=" ")
            head=head.next
        print()
    def insert_at_tail(self, head, k):
        new_node=Node(k)
        if not head:
            return new_node
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
        return head

if __name__=="__main__":
    sol=Solution()
    arr=[12, 5, 8, 7, 4]
    head=sol.convert_to_dll(arr)
    print("Initial:", sol.print_dll(head))
    head=sol.insert_at_tail(head, 20)
    print("After insertion:", sol.print_dll(head))