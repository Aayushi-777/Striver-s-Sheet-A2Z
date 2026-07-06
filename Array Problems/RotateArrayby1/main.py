class Solution:
    def rotate_by_one(self, arr):
        temp=arr[0]
        n=len(arr)
        for i in range(1, n):
            arr[i-1]=arr[i]
        arr[-1]=temp
        return arr
if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3, 4, 5, 6, 7]
    print(f"Array before shifting: {arr}")
    arr1=sol.rotate_by_one(arr)
    print(f"Array after shifting: {arr1}")
    