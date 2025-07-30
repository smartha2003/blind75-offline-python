def GroupAnagrams(strs: list[str]) -> list[list[str]]:
    hashmap = {}
    for i in strs:
        count = {}
        for char in i: # O(n)
            count[char] = count.get(char, 0) + 1

        tup = tuple(sorted(count.items())) 

        if tup in hashmap:
            hashmap[tup].append(i)
        else:
            hashmap[tup] = [i] 

    print(hashmap.values())
    return list(hashmap.values())

result = GroupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)