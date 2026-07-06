class Solution:
    def longest_consec(self, arr):
        longest=1
        st=set()
        n=len(arr)
        for num in arr:
            st.add(num)
        for i in st:
            if i-1 not in st:
                cnt=1
                x=i
                while x+1 in st:
                    x=x+1
                    cnt+=1
                longest=max(longest, cnt)
        return longest

if __name__=="__main__":
    sol=Solution()
    arr=[100, 4, 200, 1, 3, 2]
    longest=sol.longest_consec(arr)
    print(f"The longest subarray with consecutive elements has {longest} elements")