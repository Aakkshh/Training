def find_combinations(nums, target):
    def backtrack(remain, start, path):
        if remain == 0:
            result.append(path)
            return
        elif remain < 0:
            return
        for i in range(start, len(nums)):
            backtrack(remain - nums[i], i, path + [nums[i]])

    result = []
    backtrack(target, 0, [])
    return result

nums = (2, 3, 5, 7)
target = 10
combinations = find_combinations(nums, target)

print(combinations)