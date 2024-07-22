from itertools import permutations
def generate(nums):
    return list(permutations(nums))

nums = [1, 2, 3]
print(generate(nums)) 
