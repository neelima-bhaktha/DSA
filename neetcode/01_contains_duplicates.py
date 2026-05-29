def contains_duplicates(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

assert contains_duplicates([1,2,3,4])==False
assert contains_duplicates([1,2,2,3])==True
print("all test cases passed")
