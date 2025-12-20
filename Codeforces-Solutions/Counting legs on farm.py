import sys 
import math
input = sys.stdin.readline
def solution():
    tcases = int(input())
    for i in range(tcases):
        legs = int(input().strip())
        if legs%2==1:
            print("0")
            continue
        a= math.ceil(legs/4)
        b=legs/2
        answer=b-a+1
        print(int(answer))
    return 
if __name__ == "__main__":
    solution()