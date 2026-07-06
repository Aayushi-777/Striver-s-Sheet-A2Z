class Solution:
    def countdigits(self, n):
        count=0
        while n>0:
            count+=1
            n//=10
        return count
if __name__=="__main__":
    sol=Solution()
    n=12345
    count=sol.countdigits(n)
    print(f"N: {count}")

        