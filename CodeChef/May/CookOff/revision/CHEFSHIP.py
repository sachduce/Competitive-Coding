if __name__ == "__main__":
    for _ in range(int(input())):
        S = input();
        stringLength = len(S);
        count = 0;
        i = 1;
        isEqual = True;
        for k in range(stringLength-1):
            if S[k] != S[k+1]:
                isEqual = False;
                break
        if(isEqual):
            print(stringLength//2 -1);
        else:
            while(i < stringLength and S[i] != S[0]):
                i += 1;
            if(i != stringLength):
                j =i;
                s1 = S[0: i];
                count =1;
                while(j+i <= stringLength and S[j: j+i] == s1):
                    count +=1;
                    j += i;
                if(j == stringLength):
                    count = count//2 -1;
                else:
                    count = 0;
                    for i in range(1, stringLength//2):
                        if(S[0:i] == S[i: 2*i] and S[2*i : i+stringLength//2 ] == S[i+stringLength//2:]):
                            count +=1;

            print(count);