class Solution:
    def four_sum(self, arr, target):
        ans=[]
        n=len(arr)
        arr.sort()
        for i in range(n):
            if i>0 and arr[i]==arr[i-1]:
                continue
            for j in range(i+1, n):
                if j>i and arr[j]==arr[j-1]:
                    continue
                left, right=j+1, n-1
                while left<right:
                    total=arr[i]+arr[j]+arr[left]+arr[right]
                    if total==target:
                        ans.append([arr[i], arr[j], arr[left], arr[right]])
                        left+=1
                        right-=1
                        while left<right and arr[left]==arr[left-1]:
                            left+=1
                        while left<right and arr[right]==arr[right+1]:
                            right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return ans
        
if __name__=="__main__":
    sol=Solution()
    arr=[1, 0, -1, 0, -2, 2]
    target=0
    ans=sol.four_sum(arr, target)
    print("The quadruplets with the target sum in the array are:", *ans)