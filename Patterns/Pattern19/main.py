class Solution:
    def pattern(self, n):
        spaces=0
        for i in range(n):
            for j in range(n-i):
                print("*", end="")
            for j in range(spaces):
                print(" ", end="")
            for j in range(n-i):
                print("*", end="")
            print()
            spaces+=2 
        spaces=2*(n-1)
        for i in range(1, n+1):
            for j in range(1, i+1):
                print("*", end="")
            for j in range(1, spaces+1):
                print(" ", end="")
            for j in range(1, i+1):
                print("*", end="")
            print()
            spaces-=2
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
"""