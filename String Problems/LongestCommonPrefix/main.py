class Solution:
    def longest_prefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        first=strs[0]
        last=strs[-1]
        ans=""
        for i in range(min(len(first), len(last))):
            if first[i]!=last[i]:
                return ans
            ans+=first[i]
        return ans

if __name__=="__main__":
    sol=Solution()
    strs=["interview", "internet", "internal", "interval"]
    ans=sol.longest_prefix(strs)
    print(f"The longest prefix is: {ans}")