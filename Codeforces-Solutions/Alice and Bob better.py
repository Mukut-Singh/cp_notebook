import sys

def solution():
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        t_cases = int(next(iterator))
    except StopIteration:
        return

    results = []

    for _ in range(t_cases):
        n = int(next(iterator))
        a = int(next(iterator))
        
        count_less = 0
        count_greater = 0
        
        for _ in range(n):
            val = int(next(iterator))
            if val < a:
                count_less += 1
            elif val > a:
                count_greater += 1
        if count_less > count_greater:
            results.append(str(a - 1))
        else:
            results.append(str(a + 1))

    print('\n'.join(results))

if __name__ == "__main__":
    solution()