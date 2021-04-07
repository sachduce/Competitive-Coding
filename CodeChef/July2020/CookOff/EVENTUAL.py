if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        s= input();
        hashS = {};
        for v in s:
            if v in hashS:
                hashS[v] += 1;
            else:
                hashS[v] = 1;
        flag = True;
        for key in hashS.keys():
            if hashS[key]%2 == 1:
                flag = False;
                break;
        print(flag);