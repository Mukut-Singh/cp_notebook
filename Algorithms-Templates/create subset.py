def get_subsets(nums):
    n = len(nums)
    # Total subsets = 2^n
    subset_ct = 1 << n
    subsets = []
    
    # Iterate through every number from 0 to (2^n - 1)
    for mask in range(subset_ct):
        subset = []
        for i in range(n):
            # If the i-th bit of the mask is set, include nums[i]
            if (mask & (1 << i)) != 0:
                subset.append(nums[i])
        
        subsets.append(subset)
        
    return subsets

# Example Usage:
nums = [1, 2, 3]
print(get_subsets(nums))
