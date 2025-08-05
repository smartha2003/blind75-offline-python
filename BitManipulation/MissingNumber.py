def MissingNumbers(nums: list[int]) -> int:
    res = len(nums)
    for i in range(len(nums)):
        res += i - nums[i]

    return res


nums = [3,0,1]
result = MissingNumbers(nums)
print(result)