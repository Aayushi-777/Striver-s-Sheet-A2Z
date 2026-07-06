class Solution:
    def count_partitions(self, a, max_sum):
        partitions=1
        subarray_sum=0
        for num in a:
            if subarray_sum+num<=max_sum:
                subarray_sum+=num
            else:
                partitions+=1
                subarray_sum=num
        return partitions
    def largest_subarray_sum_minimized(self, a, k):
        low, high=max(a), sum(a)
        while low<=high:
            mid=(low+high)//2
            partitions=self.count_partitions(a, mid)
            if partitions>k:
                low=mid+1
            else:
                high=mid-1
        return low
    
if __name__=="__main__":
    sol=Solution()
    arr=[10, 20, 30, 40]
    k=2
    partitions=sol.largest_subarray_sum_minimized(arr, k)
    print(f"The maximum sum is: {partitions}")

    # Another version of this problem is known as the Painter's Problem