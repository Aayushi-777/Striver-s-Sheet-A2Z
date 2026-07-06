class Solution:
    def count_students(self, arr, pages):
        n=len(arr)
        students=1
        pages_stu=0
        for i in range(n):
            if pages_stu+arr[i]<=pages:
                pages_stu+=arr[i]
            else:
                students+=1
                pages_stu=arr[i]
        return students
    def find_pages(self, arr, n, m):
        if m>n:
            return -1
        low=max(arr)
        high=sum(arr)
        while low<=high:
            mid=(low+high)//2
            students=self.count_students(arr, mid)
            if students>m:
                low=mid+1
            else:
                high=mid-1
        return low

if __name__=="__main__":
    sol=Solution()
    arr=[25, 46, 28, 49, 24]
    n=5
    m=4
    ans=sol.find_pages(arr, n, m)
    print(f"The minimum pages assigned to student is: {ans}")
