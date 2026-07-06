class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def reverse_k_group(self, head, k):
        dummy=Node(0)
        dummy.next=head
        group_prev=dummy
        while True:
            kth=self.get_kth_node(group_prev, k)
            if not kth:
                break
            group_next=kth.next
            prev=group_next
            curr=group_prev.next
            for _ in range(k):
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=group_prev.next
            group_prev.next=kth
            group_prev=temp
        return dummy.next
    def get_kth_node(self, curr, k):
        while curr and k>0:
            curr=curr.next
            k-=1
        return curr
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
    head.next.next=Node(3)
    head.next.next.next=Node(4)
    head.next.next.next.next=Node(5)
    k=2
    res=sol.reverse_k_group(head, k)
    sol.print_ll(res)