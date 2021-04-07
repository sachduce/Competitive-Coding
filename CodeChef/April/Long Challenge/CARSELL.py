from sys import stdin

modulo = 10**9 + 7;

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input());
        P = sorted(list(map(int, stdin.readline().split())), reverse= True);
        sum = P[0];
        for i in range(1, n):
            val = P[i] - i;
            if(val > 0):
                sum += P[i];
            else:
                break;

        print(sum %modulo);

