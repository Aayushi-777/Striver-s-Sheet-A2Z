class Solution:
    def divisors(self, n):
        res=[]
        for i in range(1, int(n**0.5)+1):
            if n%i==0:
                res.append(i)
                if i!=n//i:
                    res.append(n//i)
        res.sort()
        return res
    
if __name__=="__main__":
    sol=Solution()
    n=36
    ans=sol.divisors(n)
    print(f"The divisors of {n} is:", *ans)
    