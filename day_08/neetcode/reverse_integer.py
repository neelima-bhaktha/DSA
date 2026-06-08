def reverse(x):
    sign = -1 if x<0 else 1
    x = abs(x)

    rev = 0 
    while x>0:
        intt = x % 10
        rev  = rev * 10 + intt
        x = x//10
    rev = sign * rev

    if rev< -2**31 or rev>2**31-1:
        return 0
    return rev
assert reverse(123) == 321
assert reverse(-123) == -321
print("passed")