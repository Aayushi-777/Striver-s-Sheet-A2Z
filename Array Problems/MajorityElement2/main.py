class Solution:
    def majority_element(self, arr):
        n=len(arr)
        cnt1, cnt2=0, 0
        el1, el2=0, 0
        for num in arr:
            if cnt1==0 and el2!=num:
                cnt1=1
                el1=num
            elif cnt2==0 and el1!=num:
                cnt2=1
                el2=num
            elif num==el1:
                cnt1+=1
            elif num==el2:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        count1=arr.count(el1)
        count2=arr.count(el2)
        result=[]
        min=n//3
        if count1>min:
            result.append(el1)
        if count2>min and el2!=el1:
            result.append(el2)
        return result
if __name__=="__main__":
    sol=Solution()
    arr=[11, 33, 33, 11, 33, 11]
    result=sol.majority_element(arr)
    print(f"The majority elements is: {result}")