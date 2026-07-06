class Solution:
    def find_sums(self, index, curr, arr, sums):
        if index==len(arr):
            sums.append(curr)
            return
        self.find_sums(index+1, curr+arr[index], arr, sums)
        self.find_sums(index+1, curr, arr, sums)
    def subset_sums(self, arr):
        sums=[]
        self.find_sums(0, 0, arr, sums)
        sums.sort()
        return sums

if __name__=="__main__":
    sol=Solution()
    arr=[5, 2, 1]
    res=sol.subset_sums(arr)
    print(*res)