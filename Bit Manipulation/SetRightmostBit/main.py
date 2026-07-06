class Solution:
    def set_rightmost_bit(self, n):
        return n | (n+1)

if __name__=="__main__":
    sol=Solution()
    n=10
    ans=sol.set_rightmost_bit(n)
    print(f"After setting the rightmost bit number is: {ans}")