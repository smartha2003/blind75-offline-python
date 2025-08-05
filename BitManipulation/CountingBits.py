def CountingBit(n: int) -> list[int]:
    dp = [0] * (n+1)

    for i in range(n+1):
        dp[i] = dp[i >> 1] + (i & 1)

    return dp

n = 2
result = CountingBit(n)
print(result)