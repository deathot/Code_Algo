2642_设计可以求最短路径的图类



class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.g = [[inf] * n for _ in range(n)]
        for x, y, w in edges:
            self.g[x][y] = w


    def addEdge(self, e: List[int]) -> None:
        self.g[e[0]][e[1]] = e[2]


    def shortestPath(self, start: int, end: int) -> int:
        n = len(self.g)
        dis = [inf] * n
        dis[start] = 0
        vis = [False] * n
        while True:
            x = -1
            for i, (b, d) in enumerate(zip(vis, dis)):
                if not b and (x < 0 or d < dis[x]):
                    x = i
            if x < 0 or dis[x] == inf:
                return -1
            if x == end:
                return dis[x]
            vis[x] = True
            for y, w in enumerate(self.g[x]):
                if dis[x] + w < dis[y]:
                    dis[y] = dis[x] + w



# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

