class Solution:
    def next_perm(self, arr):
        n=len(arr)
        index=-1
        for i in range(n-2, -1, -1):
            if arr[i]<arr[i+1]:
                index=i
                break
        if index==-1:
            arr.reverse()
            return arr
        for i in range(n-1, index, -1):
            if arr[i]>arr[index]:
                arr[i], arr[index]=arr[index], arr[i]
                break
        arr[index+1:]=reversed(arr[index+1:])
        return arr

if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3]
    nextperm=sol.next_perm(arr)
    print(f"The next permutation is: {nextperm}")
    
