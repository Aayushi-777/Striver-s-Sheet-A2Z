class Solution:
    def pattern(self, n):
        spaces=2*(n-1)
        for i in range(1, n+1):
            for j in range(1, i+1):
                print("*", end="")
            for j in range(1, spaces+1):
                print(" ", end="")
            for j in range(1, i+1):
                print("*", end="")
            spaces-=2
            print()
        spaces=2
        for i in range(n-1, 0, -1):
            for j in range(i):
                print("*", end="")
            for j in range(spaces):
                print(" ", end="")
            for j in range(i):
                print("*", end="")
            spaces+=2
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
"""