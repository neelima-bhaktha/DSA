from collections import Counter
def valid_anagram(String1, string2):
    return Counter(String1) == Counter(string2)



assert valid_anagram("listen", "silent") == True
assert valid_anagram("apple", "steve jobs") ==  False
print("all test cases passed")
