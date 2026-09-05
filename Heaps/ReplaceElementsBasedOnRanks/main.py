class Solution:
    def replace_with_rank(self, arr):
        sorted_arr=sorted(arr)
        rank_map={}
        rank=1
        for num in sorted_arr:
            if num not in rank_map:
                rank_map[num]=rank
                rank+=1
        res=[rank_map[num] for num in arr]
        return res
if __name__=="__main__":
    sol=Solution()
    arr=[1, 5, 8, 15, 8, 25, 9]
    res=sol.replace_with_rank(arr)
    print(res)