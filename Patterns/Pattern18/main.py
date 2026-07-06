class Solution:
    def pattern(self, n):
        for i in range(n):
            start=65+(n-i-1)
            for j in range(i+1):
                print(chr(start+j), end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
E 
D E
C D E
B C D E
A B C D E
"""