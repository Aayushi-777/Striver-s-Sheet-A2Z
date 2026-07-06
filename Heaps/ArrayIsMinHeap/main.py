class Solution:
    def is_heap(self, arr):
        n=len(arr)
        for i in range(n//2):
            left=i*2+1
            if left<n and arr[i]>arr[left]:
                return False
            right=i*2+2
            if right<n and arr[i]>arr[right]:
                return False
        return True

if __name__=="__main__":
    sol=Solution()
    arr=[10, 20, 30, 21, 23]
    ans=sol.is_heap(arr)
    print(f"Is the array a Min Heap?: {ans}")