#two Sum

nums = [2,7,11,15]
target=9

def twoSum(nums, target):
    hash_map = {}

    for i,num in enumerate(nums):
        if target - num in hash_map:
            return [hash_map[target-num],i]
        hash_map[num] = i

    return []

twoSum(nums,target)