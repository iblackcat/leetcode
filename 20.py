def pair(a):
    if (a == '('):
        return ')'
    elif (a == '['):
        return ']'
    elif (a == '{'):
        return '}'
    else :
        return '?'

def isValid(s):
    stack = []
    head = -1
    for i in s:
        if (i == '(' or i == '[' or i == '{'):
            stack += i
            head += 1
        elif (head != -1 and i == pair(stack[head])):
            stack = stack[:head]
            head -= 1
        else :
            return bool(0)
    if (head != -1):
        return bool(0)
    return bool(1)

a = ""
print(isValid(a))
