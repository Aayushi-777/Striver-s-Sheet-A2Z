class Solution:
    def word_break(self, s, word_dict):
        word_set=set(word_dict)
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i]=True
                    break
        return dp[len(s)]

if __name__=="__main__":
    sol=Solution()
    print(sol.word_break("takeuforward", ["take","forward","you","u"])) 
print(sol.word_break("applepineapple", ["apple"]))                  
print(sol.word_break("catsanddogs", ["and","dogs","cats","animals"]))