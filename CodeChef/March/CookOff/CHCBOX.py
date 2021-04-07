from sys import stdin

if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input());
        A = list(map(int, stdin.readline().split()));
        max_index = [];
        temp_max = -1;
        for j in range(n):
            if(temp_max < A[j]):
                temp_max = A[j];
                max_index = [j];
            elif(temp_max == A[j]):
                max_index.append(j)

        print("max: {}".format(max_index));
        diff = 0;
        if(len(max_index) > 1):
            diff = max_index[-1] - max_index[0];

        if(n//2 > diff):
            print(n//2 - diff)
        else:
            print(0)

