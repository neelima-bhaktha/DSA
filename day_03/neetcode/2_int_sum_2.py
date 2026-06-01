def two_sum(numbers, target):
    left, right=0, len(numbers)-1
    while left<right:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left+1, right+1]
        elif sum<target:
            left +=1
        elif sum>target:
            right-=1
    return []

assert two_sum([1,2,3,4], 3) == [1,2]
print("passed")