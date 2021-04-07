from sys import stdin;

if __name__ == "__main__":
    for _ in range(int(input())):
        H, P = list(map(int, stdin.readline().split()));
        while(H >0  and P > 0):
            H -= P;
            P = P//2;

        if(H > 0):
            print(0);
        else:
            print(1)