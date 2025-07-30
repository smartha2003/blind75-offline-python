def ProductofArray(nums: list[int]) -> list[int]:
    res = [1] * (len(nums))
    print(res)

    #calculate the prefix
    for i in range(len(nums)):
        if i == 0:
            res[i] = 1
        else:
            res[i] = res[i - 1] * nums[i - 1]


    #calculate the postfix
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            postfix = 1
        else:
            res[i] *= postfix
        postfix *= nums[i]

    return res


nums = [1,2,3,4]
result = ProductofArray(nums)
print(result)
'''
nums =[1,2,3,4]
res = [1,1,1,1]

pre
res[i] = res[i-1] * nums[i-1]
res = [1, 2, 6, 24]

post
res[i] *= postfix
postfix *= nums[i]
res = [24, 12, 8, 6]

res = [24,12,8,6]

'''