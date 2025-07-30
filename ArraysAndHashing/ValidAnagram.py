def ValidAnagram(s: str, t: str) -> bool:
    hashmap1 = {}
    hashmap2 = {}

    for i in s:
        hashmap1[i] = hashmap1.get(i,0) + 1
    for i in t:
        hashmap2[i] = hashmap2.get(i,0) + 1
    
    return hashmap2 == hashmap1

s = "anagram"
t = "nagaram"
result = ValidAnagram(s,t)
print(result)