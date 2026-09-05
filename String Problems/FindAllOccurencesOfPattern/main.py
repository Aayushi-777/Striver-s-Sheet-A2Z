class Solution:
    def find_all_occurences(self, text, pattern):
        n=len(text)
        m=len(pattern)
        ans=[]
        for i in range(n-m+1):
            if text[i:i+m]==pattern:
                ans.append(i)
        return ans
if __name__=="__main__":
    sol=Solution()
    text="ababcabcababc"
    pattern="abc"
    ans=sol.find_all_occurences(text, pattern)
    print(ans)