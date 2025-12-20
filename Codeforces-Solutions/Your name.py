import sys
input = sys.stdin.readline
def solve():
    try:
        line=input().strip()
        if not line:
            return
        n=int(line)

        for i in range(n):
            length_of_string = input().strip()
            s, t = map(str, input().split())
        
            if sorted(s)==sorted(t):
                print("YES")
            else:
                print("NO")

    except ValueError:
        return 
solve()    