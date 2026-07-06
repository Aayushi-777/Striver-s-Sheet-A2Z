class Solution:
    def get_subsequences(self, s):
        res=[]
        def helper(i, curr):
            if i==len(s):
                res.append(curr)
                return
            helper(i+1, curr)
            helper(i+1, curr+s[i])
        helper(0, "")
        return res

if __name__=="__main__":
    sol=Solution()
    s="abc"
    res=sol.get_subsequences(s)
    print(res)