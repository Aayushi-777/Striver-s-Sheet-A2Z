class Solution:
    def union_of_arrays(self, arr1, arr2):
        n=len(arr1)
        m=len(arr2)
        i, j=0, 0
        Union=[]
        while i<n and j<m:
            if arr1[i]<arr2[j]:
                if not Union or Union[-1]!=arr1[i]:
                    Union.append(arr1[i])
                i+=1
            elif arr2[j]<arr1[i]:
                if not Union or Union[-1]!=arr2[j]:
                    Union.append(arr2[j])
                j+=1
            else:
                if not Union or Union[-1]!=arr1[i]:
                    Union.append(arr1[i])
                i+=1
                j+=1
        while i<n:
            if not Union or Union[-1]!=arr1[i]:
                Union.append(arr1[i])
            i+=1
        while j<m:
            if not Union or Union[-1]!=arr2[j]:
                Union.append(arr2[j]) 
            j+=1
        return Union

if __name__=="__main__":
    sol=Solution()
    arr1=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    arr2=[2, 3, 4, 5, 11, 12]
    union=sol.union_of_arrays(arr1, arr2)
    print(f"The union of arr1 and arr2 is:", union)