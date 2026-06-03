def evalRPN(tokens):
    stack = []
    for c in tokens:
        if c == "+":
            stack.append(stack.pop()+stack.pop())
        elif c == "-":
            b,a = stack.pop(), stack.pop()
            stack.append(a-b)

        elif c == "*":
            stack.append(stack.pop()*stack.pop())
        elif c=="/":
            b,a = stack.pop(), stack.pop()
            stack.append(int(float(b/a)))
        else:
            stack.append(int(c))
    return stack[0]
assert evalRPN(["1","2","+","3","*","4","-"]) == 5
print("pass")