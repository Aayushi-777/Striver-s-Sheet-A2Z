class Solution:
    def kadane_algorithm(self, arr):
        maxi=float('-inf')
        sum=0
        for i in range(len(arr)):
            sum+=arr[i]
            if sum>maxi:
                maxi=sum
            elif sum<0:
                sum=0
        return maxi
if __name__=="__main__":
    sol=Solution()
    arr=[2, 3, 5, -2, 7, -4] 
    maxi=sol.kadane_algorithm(arr)
    print(f"The maximum sum is: {maxi}")
