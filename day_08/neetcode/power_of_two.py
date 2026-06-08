def p_o_two(n):
    return n>0 and (n&(n-1))==0

assert p_o_two(1) == True
assert p_o_two(3) == False
print("pass") 