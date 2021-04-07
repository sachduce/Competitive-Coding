from sys import stdin;

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input());
        A = list(map(int, stdin.readline().split()));

        dict = {};
        prevVal = 0;
        flag = False;
        for val in A:
            curVal = val;
            if curVal != prevVal:
                if curVal in dict:
                    flag = True;
                    break;
                else:
                    dict[val] = 1;
            else:
                dict[val] += 1;

            prevVal = curVal;


        if(flag):
            print("NO");
        else:
            values = list(dict.values())
            if len(values) == len(set(values)):
                print("YES")
            else:
                print("NO");



