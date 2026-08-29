from collections import deque
class Solution:
    def count_components(self, V, edges):
        adj=[[] for i in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*V
        count=0
        for i in range(V):
            if not visited[i]:
                count+=1
                queue=deque([i])
                visited[i]=True
                while queue:
                    node=queue.popleft()
                    for j in adj[node]:
                        if not visited[j]:
                            visited[j]=True
                            queue.append(j)
        return count
if __name__=="__main__":
    sol=Solution()
    V=5
    edges=[[0, 1], [1, 2], [3, 4]]
    count=sol.count_components(V, edges)
    print(f"The number of connected components: {count}")