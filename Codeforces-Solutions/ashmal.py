import sys

# Increase recursion depth for deep recursive calls (DFS/Graphs)
sys.setrecursionlimit(2000)

def solve():
    # 1. Read ALL input at once into a list of strings
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    # 2. Create an iterator to pull data one by one
    iterator = iter(input_data)

    try:
        t_cases = int(next(iterator))
    except StopIteration:
        return

    results = []

    for _ in range(t_cases):
        n = int(next(iterator)) 
        
        # Read the array of strings for this test case
        arr = [next(iterator) for _ in range(n)]
        
        # FIX 1: Initialize s as a string, not a list
        s = ""
        
        for i in range(n):
            if i == 0:
                s = arr[i]
                continue
            
            # FIX 2: Compare the two actual outcomes
            # Option A: Put new string in FRONT (arr[i] + s)
            # Option B: Put new string in BACK (s + arr[i])
            if (arr[i] + s) < (s + arr[i]):
                s = arr[i] + s
            else:
                s = s + arr[i]
        
        # Store the result for this test case
        results.append(s)
    print(*results,sep="\n")
if __name__ == "__main__":
    solve()