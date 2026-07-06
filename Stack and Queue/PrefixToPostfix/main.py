def PrefixToPostfix(s):
    stack=[]
    for c in reversed(s):
        if c.isalnum():
            stack.append(c)
        else:
            op1=stack.pop()
            op2=stack.pop()
            stack.append(op1+op2+c)
    return stack[-1]

if __name__=="__main__":
    exp="*-A/BC-/AKL"
    print(f"Prefix expression: {exp}")
    print(f"Postfix expression: {PrefixToPostfix(exp)}")