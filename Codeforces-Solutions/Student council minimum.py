import sys 
input = sys.stdin.readline

def solution():
    tcases = int(input())
    for i in range(tcases):
        n = int(input().strip())
        # Read array of integers
        arr = list(map(int, input().split()))[:n]
        for i in range(1,n-1):
            if arr[i]==-1:
                arr[i]=0 
        if arr[0] == -1 and arr[-1] == -1:
            arr[0] = 0
            arr[-1] = 0
            
        
        elif arr[0] == -1:
            arr[0] = arr[-1]
            
        
        elif arr[-1] == -1:
            arr[-1] = arr[0]
        b = [0] * (n - 1)
        for i in range(n - 1):
            b[i] = arr[i+1] - arr[i]
        print(abs(sum(b)))
        print(*arr)
if __name__ == "__main__":
    solution()