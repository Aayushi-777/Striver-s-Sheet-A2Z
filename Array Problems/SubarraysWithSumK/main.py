class Solution:
    def subarray_sum_k(self, arr, k):
        n=len(arr)
        count=0
        for i in range(n):
            total_sum=0
            for j in range(i, n):
                total_sum+=arr[j]
                if total_sum==k:
                    count+=1
        return count

if __name__=="__main__":
    sol=Solution()
    arr=[3, 1, 2, 4]
    k=6
    count=sol.subarray_sum_k(arr, k)
    print(f"The number of subarrays with sum k is: {count}")
