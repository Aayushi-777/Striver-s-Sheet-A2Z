import math
class Solution:
    def sum_by_div(Self, arr, div):
        return sum(math.ceil(x//div) for x in arr)
    def smallest_divisor(self, arr, lim):
        if len(arr)>lim:
            return -1
        low, high=1, max(arr)
        while low<=high:
            mid=(low+high)//2
            sum=self.sum_by_div(arr, mid)
            if sum<=lim:
                high=mid-1
            else:
                low=high+1
        return low

if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3, 4, 5]
    lim=8
    ans=sol.smallest_divisor(arr, lim)
    print("The smallest divisor in the array is:", ans)   