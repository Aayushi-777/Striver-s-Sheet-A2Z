class Solution:
    def printnums(self, n):
        for i in range(1, n+1):
            print(i, end=" ")
if __name__=="__main__":
    n=5
    sol=Solution()
    result=sol.printnums(n)
    print()
