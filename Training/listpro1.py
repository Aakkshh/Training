def largest(nums):
    unique_nums = list(set(nums))
    unique_nums.sort(reverse=True)
    return unique_nums[1]

nums = [10, 20, 4, 45, 99]
print(largest(nums)) 
