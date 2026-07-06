class Solution:
    def backtrack(self, curr, open, close, n, res):
        if len(curr)==2*n:
            res.append(curr)
            return
        if open<n:
            self.backtrack(curr+'(', open+1, close, n, res)
        if close<open:
            self.backtrack(curr+')', open, close+1, n, res)
    def generate_paranthesis(self, n):
        res=[]
        self.backtrack("", 0, 0, n, res)
        return res

if __name__=="__main__":
    sol=Solution()
    res=sol.generate_paranthesis(4)
    print(res)