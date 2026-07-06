class Solution:
    def longest_subarray(self, arr, k):
        n=len(arr)
        maxlen=0
        left=0
        right=0
        sum=arr[0]
        while right<n:
            while left<=right and sum>k:
                sum-=arr[left]
                left+=1
            if sum==k:
                maxlen=max(maxlen, right-left+1)
            right+=1
            if right<n:
                sum+=arr[right]
        return maxlen
    
if __name__=="__main__":
    sol=Solution()
    arr=[10, 5, 2, 7, 1, 9]
    k=15
    maxlen=sol.longest_subarray(arr, k)
    print(f"The length of the longest subarray having sum k is: {maxlen}")

