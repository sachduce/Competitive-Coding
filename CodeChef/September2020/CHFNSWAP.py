from math import floor, sqrt;
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        s = n*(n+1)//2;
        ans = 0;
        if(s % 2 == 0):
            midIndex = floor((-1 + sqrt(4*s + 1))/2);
            mid = midIndex*(midIndex+1)//2;
            ans = n - midIndex;
            if(s//2 == mid):
                ans += (midIndex)*(midIndex-1)//2 + ans*(ans-1)//2;
        print(ans);