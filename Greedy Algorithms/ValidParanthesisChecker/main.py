class Solution:
    def valid_paranthesis(Self, str):
        min_open=0
        max_open=0
        for ch in str:
            if ch=='(':
                min_open+=1
                max_open+=1
            elif ch==')':
                min_open-=1
                max_open-=1
            else:
                min_open-=1
                max_open+=1
            if max_open<0:
                return False
            if min_open<0:
                min_open=0
        return min_open==0

if __name__=="__main__":
    sol=Solution()
    str=input()
    ans=sol.valid_paranthesis(str)
    print(f"Is it a valid paranthesis?: {ans}")