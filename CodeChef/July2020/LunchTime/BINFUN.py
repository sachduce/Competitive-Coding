from sys import stdin;

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        A = list(map(int, stdin.readline().split()));
        ref = max(A);
        ma = -10**20;

        x = bin(ref)[2:]
        for j in range(n):
            a = x + bin(A[j])[2:]
            b = bin(A[j])[2:] + x
            k = abs(int(a, 2) - int(b, 2))
            if (k > ma):
                ma = k
            print(ma)

        print(ma);

