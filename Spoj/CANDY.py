if __name__ == "__main__":
    while(True):
        n = int(input())
        count =-1
        if (n == -1):
            break
        arr = [int(input()) for i in range(n)]
        summation = sum(arr)
        if(summation % n ==0):
            count =0
            avg = summation//n;
            for ele in arr:
                if(ele - avg > 0):
                    count += ele - avg

        print(count)