class Solution:
    def is_armstrong(self, n):
        k=len(str(n))
        sum=0
        num=n
        while n>0:
            digit=n%10
            sum+=digit**k
            n//=10
        if sum==num:
            print(f"Number {num} is an Armstrong number.")
        else:
            print(f"Number {num} is not an Armstrong number.")
if __name__=="__main__":
    sol=Solution()
    n=153
    sol.is_armstrong(n)
