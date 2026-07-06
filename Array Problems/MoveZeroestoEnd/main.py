class Solution:
    def move_zeroes_to_end(self, arr):
        n=len(arr)
        j=0
        for i in range(n):
            if arr[i]!=0:
                arr[i], arr[j]=arr[j], arr[i]
                j+=1
        return arr
if __name__=="__main__":
    sol=Solution()
    arr=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
    arr1=sol.move_zeroes_to_end(arr)
    print(*arr1)