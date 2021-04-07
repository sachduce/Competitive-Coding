
def recursion(val, idx, n, s, ans):
    if(val < 0 or n <= idx):
        return;
    if val == 0:
        ans[0] += 1;
        return;
    for i in range(1, s+1):
        recursion(val - i, idx + 1, n, s + i, ans)



if __name__ == '__main__':
    n = 5;
    k = 10;
    ans = [0];
    recursion(k-1, 0, n, 1, ans);
    print(ans[0]);
