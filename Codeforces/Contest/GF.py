from sys import stdin;

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        a = list(map(int, stdin.readline().split()));
        b = list(map(int, stdin.readline().split()));
        minA = min(a);
        minB = min(b);
        ans = 0;
        for i in range(n):
            ans += max(a[i]- minA, b[i]- minB);
        print(ans);




