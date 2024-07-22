def longest_increasing_subsequence(nums):
    if not nums:
        return []
    lis = []
    
    for num in nums:
        if not lis or num > lis[-1]:
            lis.append(num)
        else:
            for i in range(len(lis)):
                if num <= lis[i]:
                    lis[i] = num
                    break
    
    return lis

nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]
print(longest_increasing_subsequence(nums)) 
