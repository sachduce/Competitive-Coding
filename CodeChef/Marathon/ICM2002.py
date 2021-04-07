from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n, k = list(map(int, stdin.readline().split()))
        b = list(map(int, stdin.readline().split()))

        sumb = sum(b)

        if(sumb % k == 0 ):
            sortB = sorted(b, reverse= True)
            diff = sortB[0] - sortB[k-1]
            lastSum = sumb - sum(sortB[:k])
            if(diff <= lastSum):
                print("YES")
            else:
                print("NO")

        else:
            print("NO")






