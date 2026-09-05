class Solution:
    def dfs(self, node, adj, visited, path):
        visited[node]=1
        path[node]=1
        for neighbour in adj[node]:
            if visited[neighbour]==0:
                if self.dfs(neighbour, adj, visited, path):
                    return True
            elif visited[neighbour]==1:
                return True
        path[node]=0
        return False
    def is_cycle(self, V, adj):
        visited=[0]*V
        path=[0]*V
        for i in range(V):
            if visited[i]==0:
                if self.dfs(i, adj, visited, path):
                    return True
        return False
if __name__=="__main__":
    sol=Solution()
    V=6
    adj=[[1], [2, 5], [3], [4], [1], []]
    ans=sol.is_cycle(V, adj)
    print(f"Is there a cycle in the directed graph?: {ans}")


