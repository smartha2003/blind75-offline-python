def Encode(nums: list[str]) -> str:
    res = ""
    for i in nums:
        res += i
        res += "*"
    return res

encodedRes = Encode(["my","name","is","bob"])
print(encodedRes)

def Decode(strstr: str) -> list[str]:
    res = []
    word = ""
    for i in strstr:
        if i != "*":
            word += i
        else:
            res.append(word) 
            word = ""
    
    return res
    

decodedRes = Decode(encodedRes)
print(decodedRes)
