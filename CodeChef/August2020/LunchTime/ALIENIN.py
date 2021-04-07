def find(x):
    can_fire = c[0]
    for i in range(len(c)):
        print("cc- {} {}".format(can_fire, x))
        if can_fire <= c[i] + d:
            can_fire = c[i] + x if can_fire < c[i] else can_fire + x
        else:
            return False
    return True
for _ in range(int(input())):
    n, d = map(int, input().split())
    c = sorted(list(map(int, input().split())));
    max_diff = 0.000001;
    lo = 0;
    hi = c[-1] + d;
    while hi - lo > max_diff:
        mid = lo + ((hi - lo) / 2);
        print("{} {}".format(lo, hi))
        if find(mid):
            lo = mid
        else:
            hi = mid
    print(lo);
