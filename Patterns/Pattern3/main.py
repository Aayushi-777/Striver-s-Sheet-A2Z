class Solution:
    def pattern(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    result=sol.pattern(n)

"""
Pattern is:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
