from sys import stdin;

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input());
        nums = sorted(list(set(list(map(int, stdin.readline().split())))));
        counter = 0;
        flag = False;
        for i in range(len(nums) -1):
            if nums[i+1] -nums[i] > 1:
                flag = True;
                break;
        if(flag):
            print("NO")
        else:
            print("YES")


