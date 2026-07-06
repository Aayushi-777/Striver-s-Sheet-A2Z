class Solution:
    def max_heapify(self, nums, n, i):
        l=i*2+1
        r=i*2+2
        largest=i
        if l<n and nums[l]>nums[largest]:
            largest=l
        if r<n and nums[r]>nums[largest]:
            largest=r
        if largest!=i:
            nums[i], nums[largest]=nums[largest], nums[i]
            self.max_heapify(nums, n, largest)
    def min_to_max_heap(self, nums):
        n=len(nums)
        for i in range(n//2-1, -1, -1):
            self.max_heapify(nums, n, i)
        return nums

if __name__=="__main__":
    sol=Solution()
    nums=[10, 20, 30, 21, 23]
    print("Max Heap: ", sol.min_to_max_heap(nums))