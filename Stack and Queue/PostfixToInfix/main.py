def PostfixToInfix(s):
    stack=[]
    for c in s:
        if c.isalnum():
            stack.append(c)
        else:
            op2=stack.pop()
            op1=stack.pop()
            stack.append("("+op1+c+op2+")")
    return stack[-1]

if __name__=="__main__":
    exp="AB*C+"
    print(f"Postfix expression: {exp}")
    print(f"Infix expression: {PostfixToInfix(exp)}")