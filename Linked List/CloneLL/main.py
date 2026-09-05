class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.random=None
class Solution:
    def clone_ll(self, head):
        if head is None:
            return None
        temp=head
        while temp:
            copy=Node(temp.data)
            copy.next=temp.next
            temp.next=copy
            temp=copy.next
        temp=head
        while temp:
            copy=temp.next
            if temp.random:
                copy.random=temp.random.next
            temp=copy.next
        temp=head
        new_head=head.next
        while temp:
            copy=temp.next
            temp.next=copy.next
            if copy.next:
                copy.next=copy.next.next
            temp=temp.next
        return new_head
    def print_ll(self, head):
        while head:
            if head.random:
                print(head.data, "-> Random:", head.random.data)
            else:
                print(head.data, "-> Random: None")
            head=head.next
if __name__=="__main__":
    sol=Solution()
    head = Node(7)
    head.next = Node(14)
    head.next.next = Node(21)
    head.next.next.next = Node(28)
    head.random = head.next.next              
    head.next.random = head                  
    head.next.next.random = head.next.next.next 
    head.next.next.next.random = head.next      
    print("Original List:")
    sol.print_ll(head)
    cloned=sol.clone_ll(head)
    print("\nCloned List:")
    sol.print_ll(cloned)  