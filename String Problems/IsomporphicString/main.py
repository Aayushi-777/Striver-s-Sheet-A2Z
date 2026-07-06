class Solution:
    def is_isomorphic(self, s, t):
        m1, m2=[0]*256, [0]*256
        n=len(s)
        for i in range(n):
            if m1[ord(s[i])]!=m2[ord(t[i])]:
                return False
            m1[ord(s[i])]=i+1
            m2[ord(t[i])]=i+1
        return True
    
if __name__=="__main__":
    sol=Solution()
    s="paper"
    t="title"
    ans=sol.is_isomorphic(s, t)
    print(f"Are the two strings isomorphic?: {ans}")