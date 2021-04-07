if __name__ == "__main__":
    k = int(input());
    for _ in range(int(input())):
        n = int(input());
        ans = [-1]*(n);
        sum = n*(n+1)//2;
        val = 0;
        if(sum%2 ==  1):
            val = 1
        last1 = n%4;
        last2 = (n-1)%4;
        last3 = (n-2)%4;
        last4 = (n-3)%4;
        fill = {last1: 1, last2:0, last3: 0, last4:1};
        for i in range(n-1, -1, -1):
            ans[i] = fill[(i+1)%4];
        print(val)
        print(''.join(map(str, ans)))
