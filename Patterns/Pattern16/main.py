class Solution:
    def pattern(self, n):
        for i in range(n):
            for j in range(i+1):
                print(chr(65+i), end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
A
B B
C C C
D D D D
E E E E E
"""