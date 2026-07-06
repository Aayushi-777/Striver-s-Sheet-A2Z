class Solution:
    def majority_element(self, arr):
        cnt=0
        el=0
        n=len(arr)
        for num in arr:
            if cnt==0:
                cnt=1
                el=num
            elif num==el:
                cnt+=1
            else:
                cnt-=1
        cnt1=arr.count(el)
        if cnt1>(n//2):
            return el
        return -1
if __name__=="__main__":
    sol=Solution()
    arr=[2, 2, 1, 1, 1, 2, 2]
    element=sol.majority_element(arr)
    print(f"The majority element is: {element}")

            