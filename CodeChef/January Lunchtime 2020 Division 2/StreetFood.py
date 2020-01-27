from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        s = [0]*n
        p = [0]*n
        v = [0]*n
        maxProfit = 0
        for j in range(n):
            s[j], p[j], v[j] = list(map(int, stdin.readline().split()))
            x= p[j]//(s[j] +1)

            maxProfit = max(maxProfit,x *v[j])

        print(maxProfit)




