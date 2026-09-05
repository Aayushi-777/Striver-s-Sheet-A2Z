class Solution:
    def longest_prefix(self, s):
        n=len(s)
        for length in range(n-1, 0, -1):
            if s[:length]==s[-length:]:
                return s[:length]
        return ""
if __name__=="__main__":
    sol=Solution()
    s="levellevel"
    ans=sol.longest_prefix(s)
    print(ans)