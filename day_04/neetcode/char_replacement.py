def char_replacement(s, k) -> int:
    count = {}
    l = 0
    res  = 0
    for r in range(len(s)):
        count[s[r]] = 1+count.get(s[r], 0)
        while(r-l+1) - max(count.values()) > k:
            count[s[l]] -= 1
            l +=1
        res = max(res, r-l+1)
    return res

assert char_replacement("ABAB", 2) == 4
assert char_replacement("ABBABBA", 1) == 5
print("passed")