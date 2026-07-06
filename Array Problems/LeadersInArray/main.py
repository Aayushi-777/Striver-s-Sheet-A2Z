class Solution:
    def leaders(self, arr):
        n=len(arr)
        leader=[]
        max_val=arr[-1]
        leader.append(arr[-1])
        for i in range(n-2, -1, -1):
            if arr[i]>max_val:
                leader.append(arr[i])
                max_val=arr[i]
        leader.reverse()
        return leader

if __name__=="__main__":
    sol=Solution()
    arr=[4, 7, 1, 0]
    leader=sol.leaders(arr)
    print(f"The leaders in the array are:", *leader)