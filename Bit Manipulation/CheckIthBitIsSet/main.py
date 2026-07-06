class Solution:
    def check_ith_bit(self, n, i):
        return n & (i>>1)!=0

if __name__=="__main__":
    sol=Solution()
    num=5
    i=2
    ans=sol.check_ith_bit(num, i)
    print(f"Is the ith bit set?: {ans}")
    