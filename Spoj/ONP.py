from sys import stdin
priorityHash = {
    '+': 1,
    '-': 1,
    '/': 2,
    '*': 2,
    '^': 3
}

if __name__ == "__main__":
    for i in range(int(input())):
        expression = stdin.readline()
        ans = ''
        stack = []
        for ele in expression:
            if(ele == '('):
                stack.append(ele)
            elif (ele == ')'):
                while (len(stack) > 0 and stack[-1] != '('):
                    ans += stack[-1]
                    del stack[-1]
                if (stack[-1] == '('):
                    del stack[-1]
            elif (ele in priorityHash):
                if (stack[-1] != '('):
                    if (priorityHash[stack[-1]] > priorityHash[ele]):
                        while (len(stack) > 0 and stack[-1] != '('):
                            ans += stack[-1]
                            del stack[-1]
                    stack.append(ele)
                else:
                    stack.append(ele)
            else:
                ans += ele

        print(ans)
