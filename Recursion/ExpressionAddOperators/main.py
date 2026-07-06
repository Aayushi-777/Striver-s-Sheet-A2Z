class Solution:
    def dfs(self, num, target, index, value, last, path, ans):
        if index==len(num):
            if value==target:
                ans.append(path)
            return
        for i in range(index, len(num)):
            if i>index and num[index]=='0':
                break
            curr=num[index:i+1]
            curr_num=int(curr)
            if index==0:
                self.dfs(num, target, i+1, curr_num, curr_num, curr, ans)
            else:
                self.dfs(num, target, i+1, value+curr_num, curr_num, path+"+"+curr, ans)
                self.dfs(num, target, i+1, value-curr_num, -curr_num, path+"-"+curr, ans)
                self.dfs(num, target, i+1, value-last+last*curr_num, last*curr_num, path+"*"+curr, ans)
    def add_operators(self, num, target):
        ans=[]
        self.dfs(num, target, 0, 0, 0, "", ans)
        return ans

if __name__=="__main__":
    sol=Solution()
    num="123"
    target=6
    res=sol.add_operators(num, target)
    for exp in res:
        print(exp)