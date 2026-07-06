class Solution:
    def pattern(self, n):
        for i in range(2*n-1):
            for j in range(2*n-1):
                top=i
                left=j
                bottom=(2*n-2)-i
                right=(2*n-2)-j
                minDist=min(top, bottom, left, right)
                print(n-minDist, end=" ")
            print()
if __name__=="__main__":
    sol=Solution()
    n=5
    sol.pattern(n)

"""
Pattern is:        
5 5 5 5 5 5 5 5 5 
5 4 4 4 4 4 4 4 5
5 4 3 3 3 3 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 2 1 2 3 4 5
5 4 3 2 2 2 3 4 5
5 4 3 3 3 3 3 4 5
5 4 4 4 4 4 4 4 5
5 5 5 5 5 5 5 5 5
"""