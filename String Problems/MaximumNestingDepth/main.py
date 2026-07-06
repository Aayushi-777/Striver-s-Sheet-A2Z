class Solution:
    def max_nesting_depth(self, s):
        p=0
        ans=0
        for ch in s:
            if ch=='(':
                p+=1
            elif ch==')':
                p-=1
            ans=max(ans, p)
        return ans

if __name__=="__main__":
    sol=Solution()
    s="(1+(2*3)+((8)/4))+1"
    ans=sol.max_nesting_depth(s)
    print(f"The maximum nesting depth of the string {s} is: {ans}")