class Solution:
    def roman_to_number(self, s):
        roman={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res=0
        n=len(s)
        i=0
        while i<n:
            if i+1<n and roman[s[i]]<roman[s[i+1]]:
                res+=roman[s[i+1]]-roman[s[i]]
                i+=2
            else:
                res+=roman[s[i]]
                i+=1
        return res
    
if __name__=="__main__":
    sol=Solution()
    s="MCMXCIV" 
    res=sol.roman_to_number(s)
    print(f"The roman {s} represents: {res}")
