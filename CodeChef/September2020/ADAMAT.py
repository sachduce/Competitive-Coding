from sys import stdin;
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        mat = [];
        for i in range(n):
            mat.append(list(map(int, stdin.readline().split())));
        ans = 0;
        for i in range(n-1, 0, -1):
            if mat[0][i] != i+1 and ans%2 ==0:
                ans += 1;
            elif mat[0][i] == i+1 and ans%2 ==1:
                ans += 1;
        print(ans);
