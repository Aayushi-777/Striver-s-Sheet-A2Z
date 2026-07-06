class Solution:
    def palindrome(self, n):
        revNum=0
        num=n
        while n>0:
            digit=n%10
            revNum=revNum*10+digit
            n//=10
        if revNum==num:
            print(f"Number {num} is a palindrome.")
        else:
            print(f"Number {num} is not a palindrome.")
if __name__=="__main__":
    sol=Solution()
    n=123454321
    sol.palindrome(n)
            