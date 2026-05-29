from collections import defaultdict
def group_anagrams(string):
    res = defaultdict(list)
    for s in string:
        key = ''.join(sorted(s))
        res[key].append(s)
    return list(res.values())

assert group_anagrams(["act", "cat", "top", "pot"]) == [["act", "cat"], ["top", "pot"]]
assert group_anagrams(["ram", "mar", "arm", "pot"]) == [["ram", "mar", "arm"], [ "pot"]]
print("passed")
