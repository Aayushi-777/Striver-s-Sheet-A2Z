class Solution:
    def remove_k_digits(self, num, k):
        stack=[]
        for digit in num:
            while stack and k>0 and stack[-1]>digit:
                stack.pop()
                k-=1
            stack.append(digit)
        while stack and k>0:
            stack.pop()
            k-=1
        res=""
        while stack:
            res+=stack.pop()
        res=res.rstrip('0')
        res=res[::-1]
        if not res:
            return "0"
        return res

if __name__=="__main__":
    sol=Solution()
    num="541892"
    k=2
    ans=sol.remove_k_digits(num, k)
    print(f"The smallest number after removing {k} digits are: {ans}")