class Solution:
    def generate_binary_strings(self, n, curr, res):
        if len(curr)==n:
            res.append(curr)
            return
        self.generate_binary_strings(n, curr+"0", res)
        if not curr or curr[-1]!='1':
            self.generate_binary_strings(n, curr+"1", res)

if __name__=="__main__":
    sol=Solution()
    n=4
    res=[]
    sol.generate_binary_strings(n, "", res)
    print(res)
