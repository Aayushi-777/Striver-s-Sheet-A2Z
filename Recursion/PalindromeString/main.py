class Solution:
    def palindromestring(self, i, s):
        if i>=len(s)//2:
            return True
        if s[i]!=s[len(s)-i-1]:
            return False
        return self.palindromestring(i+1, s)
if __name__=="__main__":
    s="madam"
    sol=Solution()
    result=sol.palindromestring(0, s)
    print(f"Is {s} a palindrome string?: {result}")