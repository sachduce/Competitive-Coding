
def solve(n, input1):
    if(n == 0):
        return '';
    ans = input1[0];
    for i in range(1, n):
        if(ans[-3:] == input1[i]):
            pass
        elif(ans[-2:] == input1[i][:2]):
            ans += input1[i][2:];
        elif(ans[-1:] == input1[i][:1]):
            ans += input1[i][1:];
        else:
            ans += input1[i]
    return ans;


if __name__ == '__main__':
    input1 = ['422', '2ya', '123', '232'];
    print(solve(4, input1));
