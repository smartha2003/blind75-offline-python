def TopKFreqElements(nums: list[int], k: int) -> list[int]:
    hashmap = {}
    for i in nums:
        hashmap[i] = hashmap.get(i,0) + 1

    sortedArr = tuple(sorted(hashmap.values()))
    print(sortedArr)
    result = []

    for i in range(k):
        result.append(sortedArr[i])
    return result

nums = [1,1,1,2,2,3]
k = 2
result = TopKFreqElements(nums, k)
print(result)