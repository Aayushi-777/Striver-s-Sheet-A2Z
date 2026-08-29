class Solution:
    def num_of_provinces(self, adj):
        n=len(adj)
        visited=[False]*n
        count=0
        def dfs(node):
            visited[node]=True
            for neighbour in range(n):
                if adj[node][neighbour]==1 and not visited[neighbour]:
                    dfs(neighbour)
        for i in range(n):
            if not visited[i]:
                count+=1
                dfs(i)
        return count
if __name__=="__main__":
    sol=Solution()
    adj=[[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]]
    ans=sol.num_of_provinces(adj)
    print(ans)