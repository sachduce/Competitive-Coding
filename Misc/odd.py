from sys import stdin

if __name__ == "__main__":
    for _ in range(int(input())):
        n, k= list(map(int, stdin.readline().split()));
        arr  = list(map(int, stdin.readline().split()));
        odd = 0;
        even = 0;
        for v in arr:
            if v % 2:
                odd += 1;
            else:
                even +=1;
        if(odd >0 and ((k<= even) or (k-even)%2)):
           print("Yes")
        else:
            print("No")

