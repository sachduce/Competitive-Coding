from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        a,b =  stdin.readline().split()
        a  =a[::-1]
        b = b[::-1]
        c = int(a) + int(b)
        print(int(str(c)[::-1]))


