from sys import stdin;
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        V = list(map(int, stdin.readline().split()));
        ansV = [1]*n;
        for i in range(n):
            maxV = max(V[:i+1]);
            minV = min(V[i:]);
            for j in range(i-1, -1, -1):
                if V[j] > minV:
                    ansV[i] += 1;
            for j in range(i+1, n):
                if maxV > V[j]:
                    ansV[i] += 1;
        minp = min(ansV);
        maxp = max(ansV);
        print("{} {}".format(minp, maxp));
