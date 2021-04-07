from sys import stdin

def divideAndConquer(arr, start, end,count):
    if(end -start > 0):
        mid = (start + end)//2

        leftCount = divideAndConquer(arr, start, mid, count)
        rightCount = divideAndConquer(arr,mid+1, end, count)
        merge(arr, start, mid, end, count)


    return count[0]

def merge(arr, start, mid, end, finalCount):

    newArr = [0]*(end- start +1)
    i = start
    j = mid +1
    k =0
    count =0

    while i < mid + 1 and j < end + 1:

        if arr[i] < arr[j]:
            newArr[k] = arr[i]
            i += 1
        else:
            newArr[k] = arr[j]
            count += j -start - k
            j += 1

        k += 1

    while i < mid +1:
        newArr[k] = arr[i]
        i += 1
        k += 1

    while j < end+1:
        newArr[k] = arr[j]
        j += 1
        k += 1

    for x in range(end, start-1, -1):
        k-=1
        arr[x] = newArr[k]

    finalCount[0] += count

    return finalCount



if __name__ == "__main__":
    for i in range(int(input())):
        empty = stdin.readline()
        n = int(input())
        arr = [int(input()) for j in range(n)]
        count = divideAndConquer(arr,0, n-1, [0])

        print(count)
