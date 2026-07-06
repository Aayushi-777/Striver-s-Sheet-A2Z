class Solution:
    def divide(self, dividend, divisor):
        if dividend==-2**31 and divisor==-1:
            return 2**31-1
        sign=-1 if (dividend<0)^(divisor<0) else 1
        n, d=abs(dividend), abs(divisor)
        ans=0
        sum=0
        while sum+d<=n:
            ans+=1
            sum+=d
        return sign*ans

if __name__=="__main__":
    sol=Solution()
    dividend=10
    divisor=3
    ans=sol.divide(-10, 3)
    print(f"The answer is: {ans}")