class BinaryHeap:
    def __init__(self, capacity):
        self.capacity=capacity
        self.size=0
        self.arr=[0]*capacity
    def parent(self, i):
        return (i-1)//2
    def left(self, i):
        return 2*i+1
    def right(self, i):
        return 2*i+2
    def insert(self, x):
        if self.size==self.capacity:
            print("Heap Overflow")
            return
        self.arr[self.size]=x
        i=self.size
        self.size+=1
        while i>0 and self.arr[self.parent(i)]>self.arr[i]:
            self.arr[i], self.arr[self.parent(i)]=self.arr[self.parent(i)], self.arr[i]
            i=self.parent(i)
    def heapify(self, i):
        smallest=i
        l=self.left(i)
        r=self.right(i)
        if l<self.size and self.arr[l]<self.arr[smallest]:
            smallest=l
        if r<self.size and self.arr[r]<self.arr[smallest]:
            smallest=r
        if smallest!=i:
            self.arr[i], self.arr[smallest]=self.arr[smallest], self.arr[i]
            self.heapify(smallest)
    def get_min(self):
        if self.size==0:
            return None
        return self.arr[0]
    def extract_min(self):
        if self.size==0:
            return None
        if self.size==1:
            self.size-=1
            return self.arr[0]
        root=self.arr[0]
        self.arr[0]=self.arr[self.size-1]
        self.size-=1
        self.heapify(0)
        return root
    def decrease_key(self, i, val):
        self.arr[i]=val
        while i>0 and self.arr[self.parent(i)]>self.arr[i]:
            self.arr[i], self.arr[self.parent(i)]=self.arr[self.parent(i)], self.arr[i]
            i=self.parent(i)
    def delete(self, i):
        self.decrease_key(i, float('-inf'))
        self.extract_min()
    def print_heap(self):
        for i in range(self.size):
            print(self.arr[i], end=" ")
        print()

if __name__=="__main__":
    bh=BinaryHeap(20)
    bh.insert(4)
    bh.insert(1)
    bh.insert(2)
    bh.insert(6)
    bh.insert(7)
    bh.insert(3)
    bh.insert(8)
    bh.insert(5)
    print("Min value is: ", bh.get_min())
    bh.insert(-1)
    print("Min value is: ", bh.get_min())
    bh.decrease_key(3, -2)
    print("Min value is: ", bh.get_min())
    bh.extract_min()
    print("Min value is: ", bh.get_min())
    bh.delete(0)
    print("Min value is: ", bh.get_min())