class Solution:
    def pattern(self, n):
        for i in range(n):
            if i%2==0:
                start=1
            else:
                start=0
            for j in range(i+1):
                print(start, end=" ")
                start=1-start
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
1 
0 1
1 0 1
0 1 0 1
1 0 1 0 1
"""