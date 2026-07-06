class Solution:
    def largest_odd_number(self, s):
        ind=-1
        for i in range(len(s)-1, -1, -1):
            if (int(s[i])%2)==1:
                return s[:i+1]
        return "No odd number"

if __name__=="__main__":
    sol=Solution()
    s="604"
    res=sol.largest_odd_number(s)
    print(f"The largest odd number in the string is: {res}")