class Solution:
    def is_anagram(self, s1, s2):
        if len(s1)!=len(s2):
            return False
        freq=[0]*26
        for ch in s1:
            freq[ord(ch)-ord('A')]+=1
        for ch in s2:
            freq[ord(ch)-ord('A')]-=1
        for count in freq:
            if count!=0:
                return False
        return True
    
if __name__=="__main__":
    sol=Solution()
    s1="INTEGER"
    s2="TEGERNI"
    ans=sol.is_anagram(s1, s2)
    print(f"Is {s2} anagram of {s1}?: {ans}")
        
    
