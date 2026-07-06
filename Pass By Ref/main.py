class Solution:
    def reverseArray(self, n:int, arr:list[int])->list[int]:
        left=0
        right=n-1
        while left<right:
            arr[left], arr[right]=arr[right], arr[left]
            left+=1
            right-=1
        return arr
if __name__=="__main__":
    n=5
    arr=[1, 2, 3, 4, 5]
    print(f"Original Array: {arr}")
    sol=Solution()
    result=sol.reverseArray(n, arr)
    print(f"Reversed Array: {result}")
