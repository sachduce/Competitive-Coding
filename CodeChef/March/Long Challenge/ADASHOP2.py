from sys import stdin

steps = [
    (1,1),
    (2,2),
    (3,1),
    (1,3),
    (2,2),
    (3,3),
    (5,1),
    (1,5),
    (3,3),
    (4,4),
    (7,1),
    (1,7),
    (4,4),
    (5,5),
    (8,2),
    (2,8),
    (5,5),
    (6,6),
    (8, 4),
    (4, 8),
    (6,6),
    (7,7),
    (8,6),
    (6,8),
    (7,7),
    (8,8)
]


if __name__ == "__main__":
    for i in range(int(input())):
        r,c = list(map(int, stdin.readline().split()))

        newSteps = []
        if(r != c):
            g = (r+c)//2
            newSteps.append((r,c))
            newSteps.append((g,g))
            newSteps.append((1, 1))
        elif(r!=1):
            newSteps.append((r, c))
            newSteps.append((1, 1))

        print(len(steps) + len(newSteps) )
        for s in newSteps:
            print("{} {}".format(s[0], s[1]))
        for s in steps:
            print("{} {}".format(s[0], s[1]))