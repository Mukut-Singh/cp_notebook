

import sys

input = sys.stdin.readline 

def solve():
    t=int(input())
    for i in range(t):
        a, b, c, d = map(int, input().split())
        if a == b == c == d:
            print("YES")
        else:
            print("NO")
    pass
solve()
