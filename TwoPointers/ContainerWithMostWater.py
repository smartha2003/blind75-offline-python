def ContainerWMostWater(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    res = 0

    while l < r:
        area = min(height[l], height[r]) * (r - l)
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1

    return res

height = [1,8,6,2,5,4,8,3,7]
result = ContainerWMostWater(height)
print(result)