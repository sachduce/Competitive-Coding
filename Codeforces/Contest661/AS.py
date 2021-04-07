from sys import stdin;

def addKey(key, val, greater):
    if val >= 8:
        greater[8].add(key);
    elif (val >= 6):
        greater[6].add(key);
    elif (val >= 4):
        greater[4].add(key);
    elif (val >= 2):
        greater[2].add(key);

def removeKey(key, value, greater):
    if (value == 8):
        greater[8].add(key);
        greater[6].remove(key);
    elif (value == 6):
        greater[6].add(key);
        greater[4].remove(key);
    elif (value == 4):
        greater[4].add(key);
        greater[2].remove(key);
    elif (value == 2):
        greater[2].add(key);

def revereRemove(key, value, greater):
    if (value == 7):
        greater[8].remove(key);
        greater[6].add(key);
    elif (value == 5):
        greater[6].remove(key);
        greater[4].add(key);
    elif (value == 3):
        greater[4].remove(key);
        greater[2].add(key);
    elif (value == 1):
        greater[2].remove(key);

if __name__ == "__main__":
    n = int(input());
    lengths = stdin.readline().split();
    lengthMap = {};
    greater = {2 : set(), 4: set(), 6: set(), 8: set()}
    for l in lengths:
        if l in lengthMap:
            lengthMap[l] += 1;
        else:
            lengthMap[l] = 1;

    for key in lengthMap:
        addKey(key, lengthMap[key], greater);
    operations = int(input());
    for _ in range(operations):
        op, val = stdin.readline().split();
        if(op == '+'):
            if val in lengthMap:
                lengthMap[val] += 1;
                removeKey(val, lengthMap[val], greater)

            else:
                lengthMap[val] = 1;
        else:
            lengthMap[val] -= 1;
            revereRemove(val, lengthMap[val], greater);

        l8 = len(greater[8]);
        l6 = len(greater[6]);
        l4 = len(greater[4]);
        l2 = len(greater[2]);
        flag = False;
        if(l8 >= 1 or (l6 >=1 and (l4>=1 or l2>=1)) or (l4 >=2) or (l4 >=1 and l2>=2)):
            flag = True;

        if(flag):
            print("YES")
        else:
            print("NO");
