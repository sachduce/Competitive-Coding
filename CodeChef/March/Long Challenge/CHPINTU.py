from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n, m = list(map(int, stdin.readline().split()))
        F = list(map(int, stdin.readline().split()))
        P = list(map(int, stdin.readline().split()))
        fruitDict = {}

        for j in range(n):
            if F[j] in fruitDict:
                fruitDict[F[j]] += P[j]
            else:
                fruitDict[F[j]] = P[j]

        minVal = 10**5;

        for k in fruitDict:
            minVal = min(minVal, fruitDict[k])

        print(minVal)


