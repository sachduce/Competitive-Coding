from sys import stdin
import queue

class Graph:
    def __init__(self, vertices):
        self.V  = vertices
        self.graph = [[] for row in range(self.V)]
    def add_ege(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)



def bfs(g, start, dis ):
    q =queue.Queue()
    q.put(start)
    dis[start] =0
    lastMarked = start
    while(not q.empty()):
        u = q.get()
        lastMarked = u
        for v in g[u]:
            if(dis[v] == -1):
                dis[v] = dis[u] +1
                q.put(v)

    return dis[lastMarked]

if __name__ == "__main__":
    n = int(input())
    g =  Graph(n)
    for i in range(n -1):
        u, v  = list(map(int, stdin.readline().split()))
        g.add_ege(u-1, v-1)
    maxDist = 0
    for j in range(n-1):
        if(len(g.graph[j]) ==1):
            dis = [-1] * n
            maxDist = max(maxDist, bfs(g.graph, j, dis))

    print(maxDist)
