class Solution:
    def longest_unique_substring(self, s):
        seen=set()
        left=0
        max_len=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            max_len=max(max_len, right-left+1)
        return max_len
    
if __name__=="__main__":
    sol=Solution()
    s="cadbzabcd"
    max_len=sol.longest_unique_substring(s)
    print(f"The maximum length is: {max_len}")
