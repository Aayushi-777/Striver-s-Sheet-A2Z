class Solution:
    def is_power_of_two(self, n):
        return n>0 and (n & (n-1))==0

if __name__=="__main__":
    sol=Solution()
    n=8
    ans=sol.is_power_of_two(n)
    print(f"Is the number power of two?: {ans}")