from sys import stdin
MAX = 10 ** 30
def calculateMinArr(spotDiff, n, c, minDist, ans):
    print("start: {}".format(minDist))
    if (c == 0):
        print("comparison {} {}".format(minDist,ans[0] ))
        ans[0] = max(ans[0], minDist[0])
        minDist[0] = MAX
        return ans[0]

    elif(c == 1):
        minDist[0] = min(sum(spotDiff[0 : n]),  minDist)
        print("c==1: {}".format(minDist))
        calculateMinArr(spotDiff, 0, 0, minDist, ans)
        return ans[0]

    elif(n == c):
        print("n==c: {}".format(minDist))
        minDist[0] =  min(minDist, *spotDiff[0 : n])
        calculateMinArr(spotDiff, 0, 0, minDist, ans)
        return ans[0]

    for i in range(n-c +1, 0, -1):

        minDist[0] = min(sum(spotDiff[-i:]), minDist[0])
        print("iterator: {} , minDist: {}".format(i,minDist))

        calculateMinArr(spotDiff, n - i, c - 1, minDist, ans)


    return ans[0]



if __name__ == "__main__":
    for i in range(int(input())):
            # n ,c = list(map(int, stdin.readline().split()))
            # spots = sorted([int(input()) for j in range(n)])
            n,c = [9,4]
            spots = sorted([1,2,3,4,5,561253 , 363636 , 343432, 9999999999])
            spotDiff = [spots[k + 1] - spots[k] for k in range(n - 1)]
            print(spotDiff)
            print(calculateMinArr(spotDiff, n - 1, c - 1, [MAX], [0]))



