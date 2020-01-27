from sys import stdin

if __name__ == "__main__":
    while (True):
        a, b, c = list(map(int, stdin.readline().split()))
        if (a == b and b == c and a == 0):
            break

        if (b - a == c - b):
            print("AP {}".format(2 * c - b))
        elif (b*b == a * c):
            print("GP {}".format(int(c * c / b)))

