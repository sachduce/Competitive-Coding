from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        empty = stdin.readline()
        n = int(stdin.readline())

        count =0
        for j in range(n):
            count += int(stdin.readline())
        if(count %n == 0):
            print("YES")
        else:
            print("NO")