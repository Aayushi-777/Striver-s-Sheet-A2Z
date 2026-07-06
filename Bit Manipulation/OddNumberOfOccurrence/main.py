class Solution:
    def single_number(self, arr):
        xorr=0
        for num in arr:
            xorr^=num
        diff_bit= xorr & -xorr
        a=b=0
        for num in arr:
            if num & diff_bit:
                a^=num
            else:
                b^=num
        return sorted([a, b])

if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 1, 3, 5, 2]
    ans=sol.single_number(arr)
    print(ans)