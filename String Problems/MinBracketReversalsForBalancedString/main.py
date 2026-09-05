class Solution:
    def min_reversals(self, exp):
        open_brackets=0
        close_brackets=0
        for ch in exp:
            if ch=='(':
                open_brackets+=1
            else:
                if open_brackets>0:
                    open_brackets-=1
                else:
                    close_brackets+=1
        if (open_brackets+close_brackets)%2!=0:
            return -1
        return ((open_brackets+1)//2)+((close_brackets+1)//2)
if __name__=="__main__":
    sol=Solution()
    exp="(()))("
    ans=sol.min_reversals(exp)
    print(ans)
