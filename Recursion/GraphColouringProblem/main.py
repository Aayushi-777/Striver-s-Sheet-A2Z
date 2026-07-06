class Solution:
    def isSafe(self, node, colour, graph, n, col):
        for i in range(n):
            if i!=node and graph[i][node]==1 and colour[i]==col:
                return False
        return True
    def solve(self, node, colour, m, N, graph):
        if node==N:
            return True
        for i in range(1, m+1):
            if self.isSafe(node, colour, graph, N, i):
                colour[node]=i
                if self.solve(node+1, colour, m, N, graph):
                    return True
                colour[node]=0
        return False
    def graph_colouring(self, graph, m, N):
        colour=[0]*N
        if self.solve(0, colour, m, N, graph):
            return True
        return False
    
if __name__=="__main__":
    sol=Solution()
    N=4
    m=3
    graph = [[False] * 101 for _ in range(101)]
    graph[0][1] = graph[1][0] = True
    graph[1][2] = graph[2][1] = True
    graph[2][3] = graph[3][2] = True
    graph[3][0] = graph[0][3] = True
    graph[0][2] = graph[2][0] = True
    ans=sol.graph_colouring(graph, m, N)
    print(f"Can graph be coloured with {m} colurs?: {ans}")
