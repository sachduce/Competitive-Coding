from sys import stdin

def processPoints(arr, n):
    curv = []
    for i in range(2, n):
        if(arr[i-1] > arr[i-2] and arr[i] < arr[i-1]):
            curv.append(i-1)
        elif(arr[i-1] < arr[i-2] and arr[i] > arr[i-1]):
            curv.append(i - 1)
        elif(arr[i-1] == arr[i-2] or arr[i] == arr[i-1]):
            curv.append(i - 1)
    curv.append(n-1)
    start = 0
    j = 0
    curvDict = {}
    while(j < n and start < len(curv)):
        if(j < curv[start]):
            curvDict[j] = curv[start]
            j +=1
        else:
            start +=1
    curvDict[n-1] = n-1
    return curvDict

def processQuery(x1, x2, y, curvDict, n, A):
    count = 0
    curvX1 = curvDict[x1]

    while(x1 < x2 and x1 != curvX1):

        if(A[x1] == y):
            count += 1;

        if(A[curvX1] == y):
            count += 1

        if(A[x1] > y and A[curvX1] < y):
            count +=1

        elif(A[x1] < y and A[curvX1] > y):
            count += 1

        x1 = curvDict[x1]
        curvX1 = curvDict[x1]

    return count


if __name__ == "__main__":
    for i in range(int(input())):
        n, q = list(map(int, stdin.readline().split()))
        A = list(map(int, stdin.readline().split()))
        curvDict = processPoints(A, n);
        for j in range(q):
            x1, x2, y = list(map(int, stdin.readline().split()))
            count = processQuery(x1-1, x2-1, y, curvDict, n-1, A)
            print(count)