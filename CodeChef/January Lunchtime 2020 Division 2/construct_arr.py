from sys import stdin
modulo = 10**9 + 7

def mul(a, b):
    ans = [[0,0], [0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ans[i][j] = (ans[i][j] +  (a[i][k] * b[k][j])) %modulo
    return ans




def solve(m, n):
    matrix = [[m-1, m-1], [1, 0]]
    if(n ==1):
        return m%modulo
    ans = [[1,0], [0,1]]
    n -=2
    while(n > 0):
        if(n% 2):
            ans = mul(matrix, ans)
        matrix = mul(matrix, matrix)
        n/=2

    val = (ans[0][0]*m)% modulo+ans[0][1];
    return (val % modulo) * m % modulo;


if __name__ == "__main__":

    for i in range(int(input())):
        n, m = list(map(int, stdin.readline().split()))
        print(solve(m, n))

