class Solution:
    def count_pairs(self, arr):
        n=len(arr)
        count=0
        for i in range(n):
            for j in range(i+1, n):
                if arr[i]>2*arr[j]:
                    count+=1
        return count
if __name__=="__main__":
    sol=Solution()
    arr=[4, 1, 2, 3, 1]
    count=sol.count_pairs(arr)
    print(f"The number of reverse pairs are: {count}")