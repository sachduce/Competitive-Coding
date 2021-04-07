from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):

        n = int(input())
        a = list(map(int, stdin.readline().split()))
        b = list(map(int, stdin.readline().split()))
        x = 0
        dicB = {}
        flag = True
        res = []

        for v in a:
            x ^= v

        for v in b:
            x ^= v
            if v in dicB:
                dicB[v] +=1
            else:
                dicB[v] =1

        for v in a:
            y = x^v
            if(y not in dicB or dicB[y] == 0):
                flag = False
                break
            dicB[y] -= 1
            res.append(y)

        if(not flag):
            print(-1)
        else:
            print(*res)







