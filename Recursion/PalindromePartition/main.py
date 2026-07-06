class Solution:
    def partition(self, s):
        res=[]
        def is_palindrome(sub):
            return sub==sub[::-1]
        def backtrack(start, path):
            if start==len(s):
                res.append(path[:])
                return 
            for end in range(start, len(s)):
                substr=s[start: end+1]
                if is_palindrome(substr):
                    path.append(substr)
                    backtrack(end+1, path)
                    path.pop()
        backtrack(0, [])
        return res

if __name__=="__main__":
    sol=Solution()
    print(*sol.partition("aabaa"))