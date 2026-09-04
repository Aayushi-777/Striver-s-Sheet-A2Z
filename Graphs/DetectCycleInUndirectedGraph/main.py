from collections import deque
class Solution:
    def check_for_cycle(self, adj, s, visited):
        q=deque()
        q.append((s, -1))
        visited[s]=True
        while q:
            node, parent=q.popleft()
            for neighbour in adj[node]:
                if not visited[neighbour]:
                    visited[neighbour]=True
                    q.append((neighbour, node))
                elif neighbour!=parent:
                    return True
        return False
    def is_cycle(self, V, adj):
        visited=[False]*V
        for i in range(V):
            if not visited[i]:
                if self.check_for_cycle(adj, i, visited):
                    return True
        return False
if __name__=="__main__":
    sol=Solution()
    V=4
    edges=[(0, 1), (0, 2), (1, 2), (2, 3)]
    adj=[[] for i in range(V)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    ans=sol.is_cycle(V, adj)
    print(f"Is there cycle in the graph?: {ans}")