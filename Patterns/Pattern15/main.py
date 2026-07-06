class Solution:
    def pattern(self, n):
        for i in range(n, 0, -1):
            for j in range(i):
                print(chr(65+j), end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
A 
A B
A B C
A B C D
A B C D E
"""