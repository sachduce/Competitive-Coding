from sys import stdin;
if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, x, y = list(map(int, stdin.readline().split()));
        if(x ==1 and y ==1):
            print(x)
        else:
            val = min(2*x, y);
            if(n*m % 2 == 0):
                print(n*m*val//2);
            else:
                ans = (n*m-1)*val//2 + min(x,y)
                print(ans)