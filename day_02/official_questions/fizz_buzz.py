def fizz_buzz(n):
    res = []
    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            res.append("fizzbuzz")
        elif i%3==0:
            res.append("fizz")
        elif i%5==0:
            res.append("buzz")
        else:
            res.append(str(i))
    return res



assert fizz_buzz(3)==["1", "2", "fizz"]
assert fizz_buzz(15) == ["1","2","fizz", "4", "buzz", "fizz", "7", "8", "fizz", "buzz", "11", "fizz", "13", "14", "fizzbuzz"]
print("all cases passed")