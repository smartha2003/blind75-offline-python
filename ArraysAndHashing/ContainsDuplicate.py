def ContainsDuplicate(nums: list[int]) -> bool:
    hashmap = {}

    for i in nums:
        if i in hashmap:
            return True
        hashmap[i] = 1

    return False

test = [1,2,3,1]
result = ContainsDuplicate(test) 
print(result)