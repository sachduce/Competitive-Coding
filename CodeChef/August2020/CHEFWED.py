from sys import stdin;
class Tree:
    def __init__(self, start, end, val):
        self.val = val;
        self.start = start;
        self.end = end;
        self.left = None;
        self.right = None;


def addNodes(root, start, end, k):
    if(k> 0):
        node = Tree(start, end, k)
        root.right = node;
        return root.right
    else:
        node = Tree(start, end, 0);
        root.left = node;
        return root.left;


if __name__ == "__main__":
    for _ in range(int(input())):
        n, k = list(map(int, stdin.readline().split()));
        friends = list(map(int, stdin.readline().split()));
        conflicts = [[0 for _ in range(n)] for _ in range(n)];
        for i in range(n):
            friendDict = {};
            friendDict[friends[i]] = 1;
            for j in range(i+1, n):
                last = 0;
                if friends[j] in friendDict:
                    friendDict[friends[j]] += 1;
                    if friendDict[friends[j]] == 2:
                        last = 2;
                    else:
                        last = 1;
                else:
                    friendDict[friends[j]] = 1;
                conflicts[i][j] = conflicts[i][j - 1] + last;

        root = Tree(0, 0, friends[0]);
        





