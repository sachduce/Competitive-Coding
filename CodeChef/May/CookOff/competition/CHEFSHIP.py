if __name__ == "__main__":
    for i in range(int(input())):
        S = input();
        stringLength = len(S);
        count = 0;
        if(stringLength == 4):
            if(S[0] ==S[1] and S[2] ==S[3]):
                count =1;
        else:
            for j in range(2,stringLength,2):
                isValid = True;
                for k in range(j//2):
                    if(S[k]!= S[k+j//2]):
                        isValid =False;
                        break;
                if(isValid):
                    lastHalf = (stringLength -j)//2;
                    for k in range(j, j+lastHalf):
                        if(S[k] != S[k + lastHalf]):
                            isValid =False;
                            break;
                if(isValid):
                    t1= S[0:j//2];
                    if(j < stringLength-j and (stringLength-j)%j ==0 ):
                        isEqual = True;
                        for m in range(j, j+lastHalf, j//2):
                            if t1 != S[m: m + j//2]:
                                isEqual = False;
                                break;
                        if(isEqual):
                            count = (stringLength-j) //j;
                        else:
                            count =1
                    else:
                        count =1
                    break;
        print(count);
