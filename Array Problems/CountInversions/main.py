class Solution:
    def merge(self, arr, low, mid, high):
        temp=[]
        left, right=low, mid+1
        inv_count=0
        while left<=mid and right<=high:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                inv_count+=(mid-left+1)
                right+=1
        while left<=mid:
            temp.append(arr[left])
            left+=1
        while right<=high:
            temp.append(arr[right])
            right+=1
        for i in range(low, high+1):
            arr[i]=temp[i-low]
        return inv_count
    
    def merge_sort(self, arr, low, high):
        inv_count=0
        if low<high:
            mid=(low+high)//2
            inv_count+=self.merge_sort(arr, low, mid)
            inv_count+=self.merge_sort(arr, mid+1, high)
            inv_count+=self.merge(arr, low, mid, high)
        return inv_count

if __name__=="__main__":
    sol=Solution()
    arr=[5, 4, 3, 2, 1]
    inv_count=sol.merge_sort(arr, 0, len(arr)-1)
    print(f"Number of inversions: {inv_count}")
