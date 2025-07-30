def ThreeSum(nums: list[int]) -> list[list[int]]:
    arr = tuple(sorted(nums))
    print(arr)
    result = []

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l, r = i + 1, len(arr) - 1
        while l < r:
            if arr[i] + arr[l] + arr[r] == 0 and arr[i-1] != arr[i]:
                result.append([arr[i], arr[l], arr[r]])
                l += 1
                r -= 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
                
            elif arr[i] + arr[l] + arr[r] < 0:
                l += 1

            elif arr[i] + arr[l] + arr[r] > 0:
                r -= 1

    return result

nums = [-1,0,1,2,-1,-4]
result = ThreeSum(nums)
print(result)