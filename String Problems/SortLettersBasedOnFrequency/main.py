class Solution:
    def frequency_sorting(self, s):
        freq=[(0, chr(i+ord('a'))) for i in range(26)]
        for ch in s:
            index=ord(ch)-ord('a')
            freq[index]=(freq[index][0]+1, ch)
        freq.sort(key=lambda x: (-x[0], x[1]))
        result=[ch for f, ch in freq if f>0]
        return result

if __name__=="__main__":
    sol=Solution()
    s="tree"
    res=sol.frequency_sorting(s)
    print(f"The string sorted based on freuqncy of occureences is: {res}")