import heapq;

if __name__ == "__main__":
    k = int(input());
    for _ in range(int(input())):
        n = int(input());
        ans = [-1]*(n+1);
        last = 1;
        division = [];
        for i in range(1, n+1):
            division.append([pow(i, k), i-1, -1]);
        while(len(division) > 1):
            a = division.pop();
            b = division.pop();

            if(a[2] > -1 and b[2]> -1):
                pass;
            elif (a[2] > -1):
                last = 1 - a[2];
                b[2] = last
                ans[b[1]] = last
            elif(b[2] > -1):
                last = 1- b[2];
                a[2] = last
                ans[a[1]] = last
            else:
                ans[a[1]] = last;
                a[2] = last
                ans[b[1]] = 1- last;
                b[2] = 1- last;
                last = 1 - last;
            diff = [a[0] - b[0], n, a[2]];
            if(diff[0] > 0):
                temp = len(division)
                for j in range(len(division)):
                    if(diff[0] < division[j][0]):
                        temp = j;
                        break;
                if(temp == len(division)):
                    division.append(diff)
                else:
                    division.insert(temp, diff);

        if(ans[0] == -1):
            ans[0] = 0;
        value = 0;
        if(len(division)):
            value = division[0][0];
        print(value)
        print(''.join(map(str, ans[:n])))



