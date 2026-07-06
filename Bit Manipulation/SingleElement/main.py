class Solution:
    def get_single_element(self, arr):
        xorr=0
        for num in arr:
            xorr^=num
        return xorr

if __name__=="__main__":
    sol=Solution()
    arr=[4, 2, 2, 1, 1]
    ans=sol.get_single_element(arr)
    print(f"The element that has occurred once in the array is: {ans}")