class Solution:
    def reverse(self, arr, start, end):
        while start<end:
            arr[start], arr[end]=arr[end], arr[start]
            start+=1
            end-=1
    def rotate_by_k(self, arr, k, direction):
        n=len(arr)
        if n==0 or k==0:
            return arr
        k=k%n
        if direction=="right":
            self.reverse(arr, 0, n-1)
            self.reverse(arr, 0, k-1)
            self.reverse(arr, k, n-1)
        elif direction=="left":
            self.reverse(arr, 0, k-1)
            self.reverse(arr, k, n-1)
            self.reverse(arr, 0, n-1)
        return arr
if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3, 4, 5, 6, 7]
    k=3
    direction="left"
    print(f"Array before shifting {k} places: {arr}")
    arr1=sol.rotate_by_k(arr, k, direction)
    print(f"Array after shifting {k} places: {arr1}")
