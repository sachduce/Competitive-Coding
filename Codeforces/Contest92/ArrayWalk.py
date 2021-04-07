from sys import stdin;

class Node:
    def __init__(self, value):
        self.val = value;
        self.left = None;
        self.right = None;



def prepareTree(root, k, z, a, curr, isLeft, n, ans):
    if(k > 0):
        if(z > 0 and curr > 0 and isLeft == False):
            if(not root.left):
                root.left =  Node(a[curr-1] + root.val);
                if(k ==1):
                    ans[0] = max(ans[0], a[curr-1] + root.val)
                else:
                    root.left = prepareTree(root.left, k-1, z-1, a, curr-1, True, n, ans);
        if(curr < n):
            if(not root.right):
                root.right = Node(a[curr+1] + root.val);
                if (k == 1):
                    ans[0] = max(ans[0], a[curr+1] + root.val)
                else:
                    root.right = prepareTree(root.right, k-1, z, a, curr+1, False, n, ans);
    return root


if __name__ == "__main__":
    for _ in range(int(input())):
        n, k, z = list(map(int, stdin.readline().split()));
        a  = list(map(int, stdin.readline().split()));
        root = Node(a[0]);
        ans = [0];
        prepareTree(root, k, z, a, 0, False, n, ans);
        print(ans[0]);








