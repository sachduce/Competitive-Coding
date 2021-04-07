from sys import stdin

if __name__ == "__main__":
    n, k= list(map(int, stdin.readline().split()));
    inputList = list(map(int, stdin.readline().split()));
    result = sorted([inputList[i+1]**2- inputList[i]**2 for i in range(n-1)], reverse=True);
    print(result);
    print(sum(result[:n-k-1]));
