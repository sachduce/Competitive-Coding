from sys import stdin;
Modulo =10**9 +7;
def countBits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1

    return count

if __name__ == "__main__":

    for i in range(int(input())):
        n = int(input());
        B = list(map(int, stdin.readline().split()));
        ans = 1;
        flag = False
        for j in range(n-1):
            if((B[j] & B[j + 1]) != B[j]):
                ans = 0;
                flag = True;
                break;

        c = 0;
        if not flag:
            for j in range(n-1):
                c += bin(B[i]).count('1');
            ans = pow(2, c, Modulo)
            print(ans)


        else:
            print(0);