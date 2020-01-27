from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n,a,b,c = list(map(int, stdin.readline().split()))
        f = list(map(int, stdin.readline().split()))
        minDist = 10**10;
        for j in range(n):
            x = abs(f[j] - b) + abs(f[j] -a) +c
            minDist = min(minDist, x)


        print(minDist)




