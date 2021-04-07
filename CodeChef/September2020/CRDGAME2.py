from sys import stdin;

MOD = (10 ** 9) + 7
MAX_SIZE = (10 ** 5) + 1
factorial = [1] * MAX_SIZE
inverse_factorial = [1] * MAX_SIZE

for i in range(2, MAX_SIZE):
    factorial[i] = factorial[i-1] * i % MOD
    inverse_factorial[i] = pow(factorial[i], MOD - 2, MOD)


powDp = {};
def powerMod(k):
    if k in powDp:
        return powDp[k];
    powDp[k] = pow(2, k, MOD);
    return powDp[k];

if __name__ == "__main__":
    facDp = {0: 1, 1: 1, 2: 2};
    for _ in range(int(input())):
        n = int(input());
        C = list(map(int, stdin.readline().split()));
        Cdict = {};
        maxC = 0;
        for c in C:
            maxC = max(c, maxC);
            if c in Cdict:
                Cdict[c] += 1;
            else:
                Cdict[c] = 1;
        k = Cdict[maxC];
        if(k%2 ==0):
            half, full = inverse_factorial[k//2], factorial[k];
            ans = (powerMod(n) + (-full*pow(half, 2)* powerMod(n-k))%MOD)%MOD
        else:
            ans = powerMod(n);
        print(ans);

