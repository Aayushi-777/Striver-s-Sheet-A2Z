"""
class Solution:
    def freq_one(self, arr):
        maxi=max(arr)
        hash_arr=[0]*(maxi+1)
        for num in arr:
            hash_arr[num]+=1
        for num in arr:
            if hash_arr[num]==1:
                return num
        return -1
if __name__=="__main__":
    sol=Solution()
    arr=[4, 2, 2, 1, 1]
    num=sol.freq_one(arr)
    print(f"The number with frequency 1 in the array is: {num}")

    OR

"""
class Solution:
    def freq_one(self, arr):
        xorr=0
        n=len(arr)
        for i in range(n):
            xorr^=arr[i]
        return xorr
if __name__=="__main__":
    sol=Solution()
    arr=[4, 2, 2, 1, 1]
    num=sol.freq_one(arr)
    print(f"The number with frequency 1 in the array is: {num}")
