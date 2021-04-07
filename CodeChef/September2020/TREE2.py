from sys import stdin;
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        A = list(map(int, stdin.readline().split()));
        Aset = set();
        for a in A:
            if a > 0:
                Aset.add(a);
        print(len(Aset));
