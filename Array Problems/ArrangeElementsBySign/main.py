class Solution:
    def element_by_sign(self, arr):
        pos_ind=0
        neg_ind=1
        n=len(arr)
        ans=[0]*n
        for i in range(n):
            if arr[i]>0:
                ans[pos_ind]=arr[i]
                pos_ind+=2
            else:
                ans[neg_ind]=arr[i]
                neg_ind+=2
        return ans

if __name__=="__main__":
    sol=Solution()
    arr=[7, -1, -5, -3, 6, 4] 
    max_profit=sol.element_by_sign(arr)
    print(f"The rearranged array is: {max_profit}")