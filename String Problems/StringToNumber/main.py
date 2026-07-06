class Solution:
    def helper(self, s, i, num, sign):
        INT_MAX=2**31-1
        INT_MIN=-2**31
        if i>=len(s) or not s[i].isdigit():
            return sign*num
        num=num*10+int(s[i])
        if sign*num>=INT_MAX: return INT_MAX
        if sign*num<=INT_MIN: return INT_MIN
        return self.helper(s, i+1, num, sign)
    def string_to_number(self, s):
        i=0
        while i<len(s) and s[i]==' ':
            i+=1
        sign=1
        if i<len(s) and s[i]=='+':
            sign=1
            i+=1
        elif i<len(s) and s[i]=='-':
            sign=-1
            i+=1
        return self.helper(s, i, 0, sign)

if __name__=="__main__":
    sol=Solution()
    s="  -12345"
    res=sol.string_to_number(s)
    print(f"The integer is: {res}")
    