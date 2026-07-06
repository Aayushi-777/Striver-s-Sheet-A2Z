class Node:
    def __init__(self, data=0):
        self.data=data
        self.next=None
class Solution:
    def add_two_ll(self, l1, l2):
        dummy=Node()
        temp=dummy
        carry=0
        while (l1 is not None or l2 is not None) or carry:
            sum_val=0
            if l1 is not None:
                sum_val+=l1.data
                l1=l1.next
            if l2 is not None:
                sum_val+=l2.data
                l2=l2.next
            sum_val+=carry
            carry=sum_val//10
            node=Node(sum_val%10)
            temp.next=node
            temp=temp.next
        return dummy.next
    def create_list(self, arr):
        head=Node(arr[0])
        temp=head
        for i in arr[1:]:
            temp.next=Node(i)
            temp=temp.next
        return head
    def print_ll(self, head):
        temp=head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    num1=[2, 4, 3]
    num2=[5, 6, 4]
    l1=sol.create_list(num1)
    l2=sol.create_list(num2)
    res=sol.add_two_ll(l1, l2)
    print(f"The sum of the two linked list is:")
    sol.print_ll(res)