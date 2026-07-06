class Solution:
    def fibonacci(self, n):
        first=0
        second=1
        if n<=0:
            return
        for i in range(1, n+1):
            sum=0
            if i==1:
                print(first, end=" ")
            elif i==2:
                print(second, end=" ")
            else:
                sum=first+second
                print(sum, end=" ")
                first=second
                second=sum
if __name__=="__main__":
    n=10
    sol=Solution()
    sol.fibonacci(n)