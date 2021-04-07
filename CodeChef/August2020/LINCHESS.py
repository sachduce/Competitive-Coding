from sys import stdin;

if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = list(map(int, stdin.readline().split()));
        p = list(map(int, stdin.readline().split()));
        moves = 10**9;
        ans = -1
        for v in p:
            if k % v==0:
                if(moves > k//v -1):
                    moves = k//v -1;
                    ans = v;
                    if moves == 0:
                        break;

        print(ans);