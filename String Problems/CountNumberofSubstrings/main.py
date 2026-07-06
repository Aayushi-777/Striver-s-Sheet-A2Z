class Solution:
    def at_most_k_distinct(self, s, k):
        left, res=0, 0
        freq={}
        for right in range(len(s)):
            freq[s[right]]=freq.get(s[right], 0)+1
            while len(freq)>k:
                freq[s[left]]-=1
                if freq[s[left]]==0:
                    del freq[s[left]]
                left+=1
            res+=(right-left+1)
        return res
    def count_substrings(self, s, k):
        return self.at_most_k_distinct(s, k)-self.at_most_k_distinct(s, k-1)

if __name__=="__main__":
    sol=Solution()
    s="pqpqs"
    k=2
    print("Count:", sol.count_substrings(s, k))