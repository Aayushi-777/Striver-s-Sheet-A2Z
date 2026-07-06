class Solution:
    def is_odd(self, n):
        return n % 2!=0

if __name__=="__main__":
    sol=Solution()
    n=5
    ans=sol.is_odd(n)
    print(f"Is the number odd?: {ans}")