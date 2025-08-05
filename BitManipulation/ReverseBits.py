def ReverseBits(n: int) -> int:
    res = 0
    for i in range(32):                 # visit every bit position
        bit = (n >> i) & 1              # 1. grab i‑th bit of n
        res += bit << (31 - i)          # 2. place it at mirrored spot
    return res


n = 43261596
result = ReverseBits(n)
print(result)