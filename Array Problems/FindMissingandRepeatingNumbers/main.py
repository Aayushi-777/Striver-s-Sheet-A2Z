class Solution:
    def finding_missing_repeating(self, arr):
        n=len(arr)
        xorr=0
        for i in range(n):
            xorr^=arr[i]
            xorr^=(i+1)
        number=xorr & -xorr
        zero=0
        one=0
        for i in range(n):
            if arr[i] & number:
                one^=arr[i]
            else:
                zero^=arr[i]
            if (i+1) & number:
                one^=(i+1)
            else:
                zero^=(i+1)
        if arr.count(zero)==2:
            return [zero, one]
        return [one, zero]

if __name__=="__main__":
    sol=Solution()
    arr=[3, 1, 2, 5, 4, 6, 7, 5]
    ans=sol.finding_missing_repeating(arr)
    print(f"The repating and missing numbers are: {ans}")
        