class Solution:
    def count_and_say(self, n):
        result="1"
        for i in range(1, n):
            curr=""
            count=1
            for j in range(1, len(result)):
                if result[j]==result[j-1]:
                    count+=1
                else:
                    curr+=str(count)+result[j-1]
                    count=1
            curr+=str(count)+result[-1]
            result=curr
        return result
if __name__=="__main__":
    sol=Solution()
    n=5
    ans=sol.count_and_say(n)
    print(f"Count and say term {n}: {ans}")