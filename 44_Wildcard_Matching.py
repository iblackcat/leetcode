def isMatch(s, p):
    flag = True
    ls = len(s)
    lp = len(p)
    starts = 0
    ends = 0
    startp = 0
    endp = 0
    for i in range(0,ls):
        if (i >= lp or (p[i] != '*' and p[i] != '?' and p[i] != s[i])):
            return False
        if (p[i] == '*'):
            starts = i
            startp = i+1
            flag = False
            break
    if (flag):
        for i in range(ls,lp):
            if (p[i] != '*'):
                return False
        return True
    flag = True
    for i in range(0,ls):
        if (p[lp-1-i] == '*'):
            ends = ls-i
            endp = lp-i
            flag = False
            break
        elif (p[lp-1-i] != s[ls-1-i] and p[lp-1-i] != '?'):
            return False
    if (flag):
        for i in range(0,lp-ls):
            if (p[i] != '*'):
                return False
        return True

    print starts, ends
    if (ends < starts):
        return False
    
    model = []
    start = startp
    for i in range(startp, endp):
        if (p[i] == '*'):
            if (start != i):
                model += [p[start:i]]
            start = i+1

    if (model == []):
        return True
    past = []
    for string in model:
        tmp = []
        l = len(string)
        i = 0
        tmp += [0]
        for j in range(1,l):
            if (string[j] == string[i] or string[i] == '?' or string[j] == '?'):
                tmp += [i+1]
                i += 1
            elif (string[j] == string[0] or string[j] == '?' or string[0] == '?'):
                tmp += [1]
                i = 1
            else :
                tmp += [0]
                i = 0
        past += [tmp]

    now = 0
    su = len(model)
    i = starts
    j = 0
    while (i <= ends):
        if (j >= len(model[now])):
            now += 1
            j = 0
            if (now >= su):
                return True
        if (i == ends):
            return False
        if (s[i] == model[now][j] or model[now][j] == '?'):
            i += 1
            j += 1
        elif (j > 0 and past[now][j-1] > 0):
            j = past[now][j-1]
        elif (s[i] == model[now][0] or model[now][0] == '?'):
            i += 1
            j = 1
        else:
            i += 1
            j = 0
    
#print isMatch('aa', 'a')
#print isMatch('aa', 'aa')
#print isMatch('aaa', 'aa')
#print isMatch('aa', '*')
#print isMatch('aa', 'a*')
#print isMatch('aa', '?*')
#print isMatch('aab', 'c*a*b')
#print isMatch('aa', '***aa')
#print isMatch('aa', 'aa*aa')
#print isMatch('aa', 'aa*a')
#print isMatch('aa', 'a*aa')
#print isMatch('aaabcbcabcabcadc', 'a*abc*adc')
#print isMatch('aa', 'a')
#print isMatch('aa', 'a')

print isMatch('aabcdsbcdbcdbcdawefbdsefiuawef', 'a*a')
print isMatch('aabcdsbcdbcdbcdawefbdsefiuawef', 'a*f')
print isMatch('aabcdsbcdbcdbcdawefbdsefiuawef', 'a*ef')
print isMatch("abefcdgiescdfimde","ab*cd?i*de")
print isMatch('abcd', 'abc*d')
print isMatch('aa', 'aa*a')
print isMatch('aa', 'a*a')
