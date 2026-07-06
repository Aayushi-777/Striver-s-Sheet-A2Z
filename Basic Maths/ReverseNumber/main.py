class Solution:
    def reversenumber(self, n):
        revNum=0
        while n>0:
            digit=n%10
            revNum=revNum*10+digit
            n//=10
        return revNum
if __name__=="__main__":
    n=12345
    sol=Solution()
    revNum=sol.reversenumber(n)
    print(revNum)
