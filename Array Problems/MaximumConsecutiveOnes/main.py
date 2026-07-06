class Solution:
    def max_consec_ones(self, arr):
        n=len(arr)
        count=0
        max_count=0
        for i in range(n):
            if arr[i]==1:
                count+=1
            else:
                count=0
            max_count=max(count, max_count)
        return max_count
if __name__=="__main__":
    sol=Solution()
    arr=[1, 1, 0, 1, 1, 1, 0, 0, 1]
    max_count=sol.max_consec_ones(arr)
    print(f"The maximum consecutive ones are: {max_count}")
