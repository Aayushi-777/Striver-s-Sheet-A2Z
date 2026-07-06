class Solution:
    def square_root(self, n):
        low, high=0, n//2
        root=0
        while low<=high:
            mid=(low+high)//2
            if mid*mid<=n:
                root=mid
                low=mid+1
            else:
                high=mid-1
        return root

if __name__=="__main__":
    sol=Solution()
    n=25
    sq_root=sol.square_root(n)
    print(f"The square root of {n} is: {sq_root}")