def isValid(s):
    stack = []
    head = -1
    for i in s:
        if (i == '('):
            stack += i
            head += 1
        elif (head != -1 and i == ')'):
            stack = stack[:head]
            head -= 1
        else :
            return bool(0)
    if (head != -1):
        return bool(0)
    return bool(1)

def combi(p,q):
    ans = []
    st = ""
    if (p == 0):
        for i in range(0,q):
            st += ')'
        ans += [st]
    elif (q == 0):
        ans = []
    else :
        com = combi(p-1,q)
        for c in com:
            st = '('+c
            ans += [st]
        com = combi(p,q-1)
        for c in com:
            st = ')'+c
            ans += [st]
    return ans

def generateParenthesis(n):
    ans = []
    if (n == 0):
        return ans
    a = combi(n,n)
    for i in a:
        if (isValid(i)):
            ans += [i]
    return ans
    

s = []
s = generateParenthesis(3)
print(s)
#for i in range(0,len(s)):
#    print s[i]
