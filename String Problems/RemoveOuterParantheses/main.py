class Solution:
    def remove_outer_parantheses(self, s):
        result=""
        level=0
        for ch in s:
            if ch=='(':
                if level>0:
                    result+=ch
                level+=1
            elif ch==')':
                level-=1
                if level>0:
                    result+=ch
        return result
    
if __name__=="__main__":
    sol=Solution()
    s="(()())(())"
    res=sol.remove_outer_parantheses(s)
    print(f"The string after removing out parantheses is: {res}")