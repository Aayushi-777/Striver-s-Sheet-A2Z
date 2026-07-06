"""
class Solution:
    def find_missing_number(self, arr):
        n=len(arr)+1
        act_sum=sum(arr)
        exp_sum=n*(n+1)//2
        missing=exp_sum-act_sum
        return missing
if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
    missing_num=sol.find_missing_number(arr)
    print(f"The missing number is: {missing_num}")

    OR
    
"""
class Solution:
    def find_missing_number(self, arr):
        n=len(arr)+1
        xor1=0
        xor2=0
        for i in range(1, n+1):
            xor1^=i
        for i in range(n-1):
            xor2^=arr[i]
        return xor1^xor2
if __name__=="__main__":
    sol=Solution()
    arr=[1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12]
    missing_num=sol.find_missing_number(arr)
    print(f"The missing number is: {missing_num}")

        
        