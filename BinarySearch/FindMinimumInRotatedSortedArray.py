def Search(nums:list[int]) -> int:
    l, r = 0, len(nums)-1
    curr_min = nums[0]

    while l < r:
        mid = l + (r-l) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else: 
            r = mid - 1

    return min(curr_min, nums[l])

nums = [3,4,5,1,2]
result = Search(nums)
print(result)