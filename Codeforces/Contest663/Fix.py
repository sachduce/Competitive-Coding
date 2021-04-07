from sys import stdin;

if __name__ == "__main__":
    for _ in range(int(input())):
        n,m = list(map(int, stdin.readline().split()));
        matrix = [];
        for i in range(n):
            matrix.append(list(stdin.readline().rstrip()));

        ans = 0;

        for i in range(n):
            for j in range(m):
                if i == n-1 and matrix[i][j] == 'D':
                    ans += 1;
                if(j == m-1 and matrix[i][j] == 'R'):
                    ans += 1;

        print(ans);



