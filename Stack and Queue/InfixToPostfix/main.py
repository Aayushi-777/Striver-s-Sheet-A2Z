def prec(c):
    if c=='^':
        return 3
    if c=='/' or c=='*':
        return 2
    if c=='+' or c=='-':
        return 1
    else:
        return -1
    
def InfixToPostfix(s):
    stack=[]
    result=""
    for c in s:
        if c.isalnum():
            result+=c
        elif c=='(':
            stack.append('(')
        elif c==')':
            while stack and stack[-1]!='(':
                result+=stack.pop()
            stack.pop()
        else:
            while stack and prec(c)<=prec(stack[-1]):
                result+=stack.pop()
            stack.append(c)
    while stack:
        result+=stack.pop()
    print(f"Postfix expression: {result}")

if __name__=="__main__":
    exp="(p+q)*(m-n)"
    print(f"Infix expression: {exp}")
    InfixToPostfix(exp)