class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def reverse(self, head):
        prev=None
        temp=head
        while temp:
            next=temp.next
            temp.next=prev
            prev=temp
            temp=next
        return prev
    def add_one(self, head):
        head=self.reverse(head)
        temp=head
        carry=1
        while temp:
            total=temp.data+carry
            temp.data=total%10
            carry=total//10
            if carry==0:
                break
            if temp.next is None:
                temp.next=Node(carry)
                break
            temp=temp.next
        return self.reverse(head)
    def print_ll(self, head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    head=Node(1)
    head.next=Node(2)
    head.next.next=Node(9)
    print("Original:", sol.print_ll(head))
    head=sol.add_one(head)
    print("After adding one:", sol.print_ll(head))