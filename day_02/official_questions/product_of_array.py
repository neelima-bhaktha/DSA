def product(nums):
    n = len(nums)
    answer = [1]*n

    left_prod = 1
    for i in range(n):
        answer[i] = left_prod
        left_prod *= nums[i]

    right_prod = 1
    for i in range(n-1, -1, -1):
        answer[i] *= right_prod
        right_prod *= nums[i]


    return answer




assert product([1,2,3,4])==[24,12, 8, 6]
print("passed all test cases")