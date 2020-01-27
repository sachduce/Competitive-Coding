from sys import stdin
import queue

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for row in range(self.V)]

    def addEdge(self, u, v):
        self.graph[u].append(v)

def bfs(g,start,dest, dis):
    q = queue.Queue()
    q.put(start)
    dis[start] = 0

    while (not q.empty()):
        u = q.get()

        for i in range(len(g[u])):
            v = g[u][i]

            if (dis[v] == -1):
                dis[v] = dis[u] + 1
                if(v == dest):
                    return dis[v]
                q.put(v)

    return -1

if __name__ == "__main__":
    for i in range(int(input())):
        n, k = list(map(int, stdin.readline().split()))
        g = Graph(n)
        for b in range(n):
            x  = stdin.readline().rstrip()
            start = b -k
            end = b+ k
            if(start < 0):
                start =0
            if(end > n-1):
                end = n-1
            for e in range(start, end+1):
                if(x[e] == '1'):
                    g.addEdge(b,e)
        dis = [-1]*n
        distance = bfs(g.graph, 0,n-1, dis )
        print(distance)