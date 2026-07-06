class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def search_element(self, head, val):
        temp=head
        while temp is not None:
            if temp.data==val:
                return True
            temp=temp.next
        return False
    
if __name__=="__main__":
    sol=Solution()
    head=Node(10)
    head.next=Node(20)
    head.next.next=Node(30)
    ans=sol.search_element(head, 40)
    print(f"Is the element in the linked list?: {ans}")