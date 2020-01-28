from sys import stdin
import math

class Point:
    def __init__(self,x, y):
        self.x = x
        self.y = y

def findDistance(point1, point2):
        return math.sqrt(pow(point1.x - point2.x, 2) + pow(point1.y - point2.y, 2))

if __name__ == "__main__":
    for i in range(int(input())):
        n, m,w, h = list(map(int, stdin.readline().split()))
        s = stdin.readline().rstrip()
        points = []
        minDist = max(w,h)*2
        u = d =h
        l = r =w

        for j in range(m):
            x,y = list(map(int, stdin.readline().split()))
            points.append(Point(x,y))
            u = min(u, h- y)
            d = min(d,  y)
            l = min(l, x)
            r = min(r, w -x)

        for p in range(m):
            for k in range(p+1,m):
                minDist = min( findDistance(points[p],points[k]), minDist)

        for f in range(n):
            if(s[f] == 'L'):
                minDist = min(minDist,2*l)
                l = r
            elif(s[f] == 'R'):
                minDist = min(minDist, 2 * r)
                r = l
            elif (s[f] == 'U'):
                minDist = min(minDist, 2 * u)
                u =d
            elif (s[f] == 'D'):
                minDist = min(minDist, 2 * d)
                d = u

        print(minDist)