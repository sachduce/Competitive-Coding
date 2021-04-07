from collections import  defaultdict, deque;
from sys import stdin;
maxint = 10**9;

def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list);

    def addEdge(self, u, v):
        self.graph[u].append(v);
        self.graph[v].append(u);

    def bfs(self, src):
        queue = deque();
        dist = [-1]*self.V;
        queue.append(src);
        dist[src] = 0;
        while(len(queue)):
            u = queue.popleft();
            for v in self.graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1;
                    queue.append(v);
        return dist


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        in_degree = [0]*n;
        graph = Graph(n);
        for _ in range(n-1):
            u, v = list(map(int, stdin.readline().split()));
            in_degree[u-1] += 1;
            in_degree[v-1] += 1;
            graph.addEdge(u-1,v-1);

        dist = graph.bfs(0);
        w = [7420738134810, 4391633, 70746471270782959]
        ans = [];
        for d in dist:
            if(d % 2 == 0):
                ans.append(w[0])
            elif(d == 1):
                ans.append(w[1]);
            else:
                ans.append(w[2]);
        print(*ans, sep = " ")


