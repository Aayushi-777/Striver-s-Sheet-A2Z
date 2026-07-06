class Solution:
    def power(self, x, n):
        if n<0:
            return 1.0/self.power(x, -n)
        elif n==0:
            return 1
        elif n==1:
            return x
        elif n%2==0:
            return self.power(x*x, n//2)
        else:
            return x*self.power(x, n-1)

if __name__=="__main__":
    sol=Solution()
    x=2.0
    n=10
    res=sol.power(x, n)
    print(f"{x} to the power of {n} is: {res}")        
        