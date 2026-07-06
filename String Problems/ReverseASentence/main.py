class Solution:
    def reverse_sentence(self, s):
        result=""
        i=len(s)-1
        while i>=0:
            while i>=0 and s[i]==" ":
                i-=1
            if i<0:
                break
            end=i
            while i>=0 and s[i]!=" ":
                i-=1
            word=s[i+1:end+1]
            if result!=" ":
                result+=" "
            result+=word
        return result

if __name__=="__main__":
    sol=Solution()
    s=" amazing coding skills "
    res=sol.reverse_sentence(s)
    print(f"After reversing the sentence: {res}")