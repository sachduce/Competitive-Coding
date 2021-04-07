from sys import stdin;

if __name__ == "__main__":
    for _ in range(int(input())):
        l, r = list(map(int, stdin.readline().split()));
        if(2*l <= r):
            print("{} {}".format(l, 2*l));
        else:
            print("-1 -1");