class Solution:
    def factorial(self, n):
        if n==0:
            return 1
        return n*self.factorial(n-1)
if __name__=="__main__":
    sol=Solution()
    n=6
    fact=sol.factorial(n)
    print(f"The factorial of {n} is: {fact}")