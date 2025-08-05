def NumOf1Bits(n : int) -> int:
    count = 0

    while n:
        n &= n-1 # Brian Kernighan Trick to set the lowest bit to 0
        count += 1
    return count

n = 33
result = NumOf1Bits(n)
print(result)