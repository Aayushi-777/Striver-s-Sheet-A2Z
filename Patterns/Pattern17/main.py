class Solution:
    def pattern(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")
            for j in range(i+1):
                print(chr(65+j), end="")
            for j in range(i-1, -1, -1):
                print(chr(65+j), end="")
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
"""