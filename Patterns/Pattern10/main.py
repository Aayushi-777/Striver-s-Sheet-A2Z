class Solution:
    def pattern(self, n):
        for i in range(n):
            for j in range(i+1):
                print("*", end="")
            print()
        for i in range(n-1):
            for j in range(n-i-1):
                print("*", end="")
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:
*
**
***
****
*****
****
***
**
*
"""