class Solution:
    def longest_palindrome(self, s):
        res=""
        n=len(s)
        def expand(l, r):
            while l>=0 and r<n and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        for i in range(n):
            for p in (expand(i, i), expand(i, i+1)):
                if len(p)>len(res):
                    res=p
        return res

if __name__=="__main__":
    sol=Solution()
    s="babad"
    res=sol.longest_palindrome(s)
    print(f"The longest palindrome in {s} is: {res}")