class Solution:
    def removeduplicates(self, arr):
        seen=set()
        index=0
        for num in arr:
            if num not in seen:
                seen.add(num)
                arr[index]=num
                index+=1
        return index
if __name__=="__main__":
    sol=Solution()
    arr=[0, 2, 2, 1, 1, 5]
    k=sol.removeduplicates(arr)
    print("k=", k)
    print(f"The array without duplicates is: {arr[:k]}")