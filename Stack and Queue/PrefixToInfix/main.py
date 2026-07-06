def PrefixToInfix(s):
    stack=[]
    for c in reversed(s):
        if c.isalnum():
            stack.append(c)
        else:
            op1=stack.pop()
            op2=stack.pop()
            stack.append("("+op1+c+op2+")")
    return stack[-1]

if __name__=="__main__":
    exp="*-A/BC-/AKL"
    print(f"Prefix expression: {exp}")
    print(f"Infix expression: {PrefixToInfix(exp)}")