from collections import defaultdict
from sys import stdin

class Graph:
    def __init__(self, v):
        self.V = v
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def printAllPathsUtil(self, u, d, visited, path, p, ans,amount):
        if(ans):
            return ans

        visited[u] = True
        path.append(u)

        if u == d:
            ans = self.processCombination(path, amount, p )
            if(ans):
                return ans
        else:
            for i in self.graph[u]:
                if visited[i] == False:
                    ans = self.printAllPathsUtil(i, d, visited, path, p, ans, amount)

        path.pop()
        visited[u] = False
        return ans



    def printAllPaths(self, s, d, p,ans):
        visited = [False] * (s +1)
        path = []
        ans = self.printAllPathsUtil(s, d, visited, path, p, ans, s)
        return ans

    def gvmakeGraph(self, coins, amount):
        for coin in coins:
            for x in range(coin, amount + 1):
                if(x-coin in self.graph):
                    self.addEdge(x, x-coin)

    def add_node(self, amount, coins):
        self.V += 1
        for coin in coins:
            if(amount-coin in self.graph):
                self.addEdge(amount, amount-coin)

    def processCombination(self, combination, amount, p):
        coinDic = {}

        for i in range(len(combination) -1):
            v = combination[i] -combination[i+1]

            if(amount - v >= p):
                return None

            if( v in coinDic ):
                coinDic[v] +=1
            else:
                coinDic[v] = 1

        return coinDic

if __name__ == "__main__":
    for i in range(int(input())):
        n, p = list(map(int, stdin.readline().split()))
        d = list(map(int, stdin.readline().split()))

        isNotFactors = -1
        isNotDivP = -1
        for i in range(n):
            if(p % d[i] != 0):
                isNotDivP = i
                break

            if(i < n-1 and d[i+1] % d[i] != 0):
                isNotFactors = i

        if(isNotFactors == -1 and isNotDivP == -1):
            print("NO")
        else:
            max_amount = p + d[-1] -1
            ans = {}
            g = Graph(p)
            g.addEdge(0,0)
            g.makeGraph(d, p)
            print("graph : {} ".format(g.graph))
            for st in range(p+1, max_amount+1):
                g.add_node(st, d)
                ans = g.printAllPaths(st, 0,p, None)
                if(ans):
                    break

            print("YES", end=' ')
            for ip in range(n):
                if d[ip] in ans:
                    print(ans[d[ip]], end=' ')
                else:
                    print(0, end=' ')

            print('')
