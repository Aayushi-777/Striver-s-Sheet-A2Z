class Solution:
    def three_sum(self, arr):
        arr.sort()
        n=len(arr)
        ans=[]
        for i in range(n):
            if i>0 and arr[i]==arr[i-1]:
                continue
            left, right=i+1, n-1
            while left<right:
                total=arr[i]+arr[left]+arr[right]
                if total==0:
                    ans.append([arr[i], arr[left], arr[right]])
                    left+=1
                    right-=1
                    while left<right and arr[left]==arr[left-1]:
                        left+=1
                    while left<right and arr[right]==arr[right+1]:
                        right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1
        return ans
    
if __name__=="__main__":
    sol=Solution()
    arr=[-1, 0, 1, 2, -1, -4]
    ans=sol.three_sum(arr)
    print("The triplets that add to 0 in the array are:")
    print(*ans)
        

