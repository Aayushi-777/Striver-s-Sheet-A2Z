def PostfixToPrefix(s):
    stack=[]
    for c in s:
        if c.isalnum():
            stack.append(c)
        else:
            op2=stack.pop()
            op1=stack.pop()
            stack.append(c+op1+op2)
    return stack[-1]

if __name__=="__main__":
    exp="ABC/-AK/L-*"
    print(f"Postfix expression: {exp}")
    print(f"Prefix exression: {PostfixToPrefix(exp)}")