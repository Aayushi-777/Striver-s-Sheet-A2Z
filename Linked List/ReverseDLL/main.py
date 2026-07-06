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
            new_node=Node(val)
            new_node.prev=prev
            prev.next=new_node
            prev=new_node
        return head
    def reverse_dll(self, head):
        temp=None
        curr=head
        while curr is not None:
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        if temp is not None:
            head=temp.prev
        return head
    def print_dll(self, head):
        while head is not None:
            print(head.data, end=" ")
            head=head.next
        print()

if __name__=="__main__":
    sol=Solution()
    arr=[10, 20, 30, 40, 50]
    head=sol.convert_to_dll(arr)
    print("Original DLL:", sol.print_dll(head))
    head=sol.reverse_dll(head)
    print("After reversing:", sol.print_dll(head))