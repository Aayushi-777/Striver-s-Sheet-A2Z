class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class Solution:
    def detect_cycle(self, head):
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
        return None

if __name__=="__main__":
    sol=Solution()
    head=Node(3)
    head.next=Node(2)
    head.next.next=Node(0)
    head.next.next.next=Node(-4)
    head.next.next.next.next=head.next
    res=sol.detect_cycle(head) 
    if res:
        print(f"Cycle starts at node: {res.data}")
    else:
        print(f"No cycle found")