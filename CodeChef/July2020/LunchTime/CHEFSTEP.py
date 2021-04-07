from sys import stdin, stdout;
if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = map(int, input().split())
        A = list(map(int, stdin.readline().split()));
        for s in A:
            if (s % k == 0):
                stdout.write('1')
            else:
                stdout.write('0')
        stdout.write('\n');
