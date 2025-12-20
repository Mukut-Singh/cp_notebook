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
        # 3. Get number of test cases
        t_cases = int(next(iterator))
    except StopIteration:
        return

    

    for _ in range(t_cases):
        # --- INPUT SECTION ---
        l  = int(next(iterator)) 
        a  = int(next(iterator)) 
        b  = int(next(iterator))
        # arr = [int(next(iterator)) for _ in range(n)]
        results = []
        # --- LOGIC SECTION ---
        for k in range(l):
            p=(a+k*b)%l 
            results.append(p)
            
        print(max(results))       
        
        # --- OUTPUT STORAGE ---
        # results.append(str(ans))

    # 4. Print all results efficiently
    

if __name__ == "__main__":
    solve()
