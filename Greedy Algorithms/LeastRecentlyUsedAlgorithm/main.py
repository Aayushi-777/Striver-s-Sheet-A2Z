class LRUCache:
    class Node:
        def __init__(self, key, data):
            self.key=key
            self.data=data
            self.next=None
            self.prev=None
    def __init__(self, capacity):
        self.head=self.Node(-1, -1)
        self.tail=self.Node(-1, -1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cap=capacity
        self.m={}
    def delete(self, del_node):
        del_prev=del_node.prev
        del_next=del_node.next
        del_prev.next=del_next
        del_next.prev=del_prev
    def add(self, new_node):
        temp=self.head.next
        new_node.next=temp
        new_node.prev=self.head
        self.head.next=new_node
        temp.prev=new_node
    def get(self, key):
        if key in self.m:
            res_node=self.m[key]
            res=res_node.data
            del self.m[key]
            self.delete(res_node)
            self.add(res_node)
            self.m[key]=self.head.next
            return res
        return -1
    def put(self, key, val):
        if key in self.m:
            existing_node=self.m[key]
            del self.m[key]
            self.delete(existing_node)
        if len(self.m)==self.cap:
            del self.m[self.tail.prev.key]
            self.delete(self.tail.prev)
        self.add(self.Node(key, val))
        self.m[key]=self.head.next

if __name__=="__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))