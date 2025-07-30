def TwoSum(nums:list[int], target:int) -> list[int]:
    hashmap = {}
    result = []

    for i in range(len(nums)):
        need = target - nums[i]
        print(need)
        if need in hashmap:
            return [hashmap[need], i]
        else:
            hashmap[nums[i]] = i
            print(hashmap)
    return result



nums = [2,7,11,15]
target = 9
result = TwoSum(nums, target)
print(result)