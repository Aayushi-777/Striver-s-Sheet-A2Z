def precedence(c):
    if c=='^':
        return 3
    elif c=='*' or c=='/':
        return 2
    elif c=='+' or c=='-':
        return 1
    return 0
def InfixToPostfix(s):
    s='('+s+')'
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
            while stack and precedence(c)<=precedence(stack[-1]):
                result+=stack.pop()
            stack.append(c)
    while stack:
        result+=stack.pop()
    return result
def InfixToPrefix(s):
    s=s[::-1]
    s=s.replace('(', 'temp').replace(')', '(').replace('temp', ')')
    s=InfixToPostfix(s)
    return s[::-1]

if __name__=="__main__":
    exp="(p+q)*(c-d)"
    print(f"Infix expression: {exp}")
    print(f"Prefix expression: {InfixToPrefix(exp)}")  