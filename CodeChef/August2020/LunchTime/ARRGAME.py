from sys import stdin;
import math;
if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        A = list(map(int, stdin.readline().split()));
        maxEmpty = 0;
        secondMaxEmpty = 0;
        temp = 0;
        for a in A:
            if a == 0:
                temp += 1;
            else:
                if(maxEmpty <= temp):
                    secondMaxEmpty = maxEmpty;
                    maxEmpty = temp;
                elif(secondMaxEmpty < temp):
                    secondMaxEmpty = temp
                temp = 0;
        if (maxEmpty <= temp):
            secondMaxEmpty = maxEmpty;
            maxEmpty = temp;
        elif (secondMaxEmpty < temp):
            secondMaxEmpty = temp
        ans = 'Yes';
        compare = math.ceil(maxEmpty/2);
        if(maxEmpty %2 ==0 or  compare <= secondMaxEmpty):
            ans = 'No';
        print(ans);
