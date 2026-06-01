def longest_consq_seq(nums):
    numset = set(nums)
    longest = 0

    for num in numset:
        if num-1 not in numset:
            length = 0
            while num+length in numset:
                length+=1
                longest = max(length, longest)
    return longest


assert longest_consq_seq([2,20,4,10,3,4,5]) == 4
print("pass")