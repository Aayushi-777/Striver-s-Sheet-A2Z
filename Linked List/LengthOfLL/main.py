class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def length_of_ll(self, head):
        count=0
        temp=head
        while temp is not None:
            count+=1
            temp=temp.next
        return count
    
if __name__=="__main__":
    sol=Solution()
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    count=sol.length_of_ll(head)
    print(f"The length of the linked list is: {count}")
