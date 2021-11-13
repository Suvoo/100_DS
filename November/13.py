x = '({[]})'

stack=[]
for i in x:
    if i =='(' or i =='{' or i =='[' :
        stack.append(i)

    if(len(stack) == 0):
        return False

    if i ==']' :
        t = stack[-1]
        stack.pop()
        if t != '[':
            return False

    if i =='}' :
        t = stack[-1]
        stack.pop()
        if t != '{':
            return False

    if i ==')' :
        t = stack[-1]
        stack.pop()
        if t != '(':
            return False

if len(stack) == 0:
    return True           
else:
    return False