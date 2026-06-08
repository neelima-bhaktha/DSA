def c_s(n):
    way = 0
    if n==1:
        return 1
    elif n==2:
        return 2
    prev1 =1
    prev2 =2 
    for i in range(3, n+1):
        way = prev1 +prev2
        prev1 = prev2
        prev2 = way
    return way

assert c_s(2) == 2
assert c_s(3) == 3
print("passed")