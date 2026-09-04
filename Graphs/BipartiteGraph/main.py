class Solution:
    def dfs(self, node, col, colour, adj):
        colour[node]=col
        for neighbour in adj[node]:
            if colour[neighbour]==-1:
                if not self.dfs(neighbour, 1-col, colour, adj):
                    return False
            elif colour[neighbour]==col:
                return False
        return True
    def is_bipartite(self, V, adj):
        colour=[-1]*V
        for i in range(V):
            if colour[i]==-1:
                if not self.dfs(i, 0, colour, adj):
                    return False
        return True
if __name__=="__main__":
    sol=Solution()
    V=4
    adj=[[] for i in range(V)]
    adj[0].append(2)
    adj[2].append(0)
    adj[0].append(3)
    adj[3].append(0)
    adj[1].append(3)
    adj[3].append(1)
    adj[2].append(3)
    adj[3].append(2)
    ans=sol.is_bipartite(V, adj)
    if ans:
        print(1)
    else:
        print(0)