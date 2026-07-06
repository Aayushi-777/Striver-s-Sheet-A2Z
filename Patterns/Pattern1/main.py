class Solution:
    def pattern(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    result=sol.pattern(n)

"""
Pattern is:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
