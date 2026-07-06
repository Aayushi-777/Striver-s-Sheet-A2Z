class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
class Solution:
    def __init__(self):
        self.head=None
    def insert_at_end(self, data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def remove_duplicates(self):
        if not self.head:
            return None
        temp=self.head
        while temp and temp.next:
            next_dist=temp.next
            while next_dist and next_dist.data==temp.data:
                next_dist=next_dist.next
            temp.next=next_dist
            if next_dist:
                next_dist.prev=temp
            temp=temp.next
        return self.head
    def print_dll(self):
        temp=self.head
        while temp:
            print(temp.data, end=" ")
            temp=temp.next
        print()

if __name__=="__main__":
    sol=Solution()
    values=[1, 2, 2, 2, 3, 4, 4, 5, 5, 6]
    for val in values:
        sol.insert_at_end(val)
    print("Original List:", sol.print_dll())
    sol.remove_duplicates()
    print("After removing duplicates:", sol.print_dll())