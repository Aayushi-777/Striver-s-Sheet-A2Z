class Solution:
    def pattern(self, n):
        spaces=2*(n-1)
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end="")
            for j in range(1, spaces+1):
                print(" ", end="")
            for j in range(i, 0, -1):
                print(j, end="")
            print()
            spaces-=2
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
1        1
12      21
123    321
1234  4321
1234554321
"""