class Solution:
    def dfs(self, node, adj, visited, res):
        visited[node]=True
        res.append(node)
        for neighbour in adj[node]:
            if not visited[neighbour]:
                self.dfs(neighbour, adj, visited, res)
if __name__=="__main__":
    sol=Solution()
    V=5
    adj=[[1, 2], [0, 3], [0, 4], [1], [2]]
    visited=[False]*V
    res=[]
    sol.dfs(0, adj, visited, res)
    print(*res)