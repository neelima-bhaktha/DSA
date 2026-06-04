def car_fleet(target, position, speed):
    pair = [(p,s ) for p,s in zip(position, speed)]
    pair.sort(reverse=True)
    stack=[]
    for p,s in pair:
        stack.append((target-p)/s)
        if len(stack) >= 2 and stack[-1]<=stack[-2]:
            stack.pop()
    return len(stack)

assert car_fleet(9, [4,1,0,7], [2,2,1,1])==4
print("pass")