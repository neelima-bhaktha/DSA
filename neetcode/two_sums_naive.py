def two_sum(nums, target):
    map = {}
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if complement in map:
            return[map[complement], i]
        map[num] = i
assert two_sum([4,5,6,7], 10) == [0,2]
assert two_sum([4,5,6,7], 12) == [1, 3]
print("all test cases passed")