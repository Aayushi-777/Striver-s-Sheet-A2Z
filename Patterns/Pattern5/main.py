class Solution:
    def pattern(self, n):
        for i in range(n, 0, -1):
            print("* "*i)
        print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:
* * * * *
* * * * 
* * *
* *
*
"""
