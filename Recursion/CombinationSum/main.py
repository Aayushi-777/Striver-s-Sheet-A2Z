class Solution:
    def combination_sum(self, arr, target):
        res=[]
        def helper(i, curr, total):
            if total==target:
                res.append(curr)
                return
            if i==len(arr) or total>target:
                return
            helper(i, curr+[arr[i]], total+arr[i])
            helper(i+1, curr, total)
        helper(0, [], 0)
        return res

if __name__=="__main__":
    sol=Solution()
    arr=[2, 3, 6, 7]
    target=7
    res=sol.combination_sum(arr, target)
    print(f"The subsequences with the sum {target} are: {res}")
