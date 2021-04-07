from sys import stdin
from collections import defaultdict

def processCombination(start, end, combinations, graph, k):
    isGreater = True;
    isLower = True;
    for j in range(k):
        if(isLower == False and isGreater == False):
            break
        if(combinations[start][j] > combinations[end][j]):
            isLower = False
        else:
            isGreater =False

    if(isLower):
        graph[end].append(start)

    if(isGreater):
        graph[start].append(end)

def getLengths(graph, lengths):
    for k in graph:
        lengths[k] = len(graph[k])



def dfs(u, vis, graph, mt):
    vis[u] =1

    for v in graph[u]:
        print("{} {} {} {} {}".format(mt[v], u, v, vis, mt));
        if(mt[v] < 1 or (vis[mt[v]] == 0 and dfs(mt[v], vis, graph, mt )) ):

            mt[v] = u

            return 1;
    return 0;



if __name__ == "__main__":
    for i in range(int(input())):
        n, k = list(map(int, stdin.readline().split()))
        combinations = {};

        for j in range(1,n+1):
            combinations[j] = [];


        temp = []
        for j in range(k):
            temp = list(map(int, stdin.readline().split()))

            for l in range(n):
                combinations[temp[l]].append(l)

        graph = defaultdict(list)


        for j in range(1,n+1):
            for l in range(j+1, n+1):
                processCombination(j, l, combinations, graph, k)
        print(graph)
        mt = [0] *(n+1);
        count =0
        for j in range(1, n+1):
            vis = [0]*(n+1)
            count += dfs(j, vis, graph, mt)

        print(n-count)
        print(*mt[1:n+1], sep=' ')