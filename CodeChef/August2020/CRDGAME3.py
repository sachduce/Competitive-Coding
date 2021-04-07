from sys import stdin;
from math import  ceil;
if __name__ == "__main__":
    for _ in range(int(input())):
        c, r = list(map(int, stdin.readline().split()));
        chef = ceil(c/9);
        rick = ceil(r/9);
        if(rick <= chef):
            print("1 {}".format(rick));
        else:
            print("0 {}".format(chef));