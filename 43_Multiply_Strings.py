def multiply(num1, num2):
    l1 = len(num1)
    l2 = len(num2)
    if (l1 == 1 and num1[0] == '0') or (l2 == 1 and num2[0] == '0'):
        return '0'
    
    flag = False
    start1 = 0
    start2 = 0
    if (num1[0] == '-'):
        flag = not flag
        start1 = 1
    if (num2[0] == '-'):
        flag = not flag
        start2 = 1

    ans = []
    l = 0

    for i in range(0,l1-start1):
        ii = l1-1-i
        c = 0
        for j in range(0,l2-start2):
            jj = l2-1-j
            if (l == i+j):
                ans += [0]
                l += 1
            tmp = ans[i+j]
            tmp += int(num1[ii])*int(num2[jj]) + c
            c = tmp / 10
            tmp %= 10
            ans[i+j] = tmp
        if (c != 0):
            if (l == i+j+1):
                ans += [c]
                l += 1
            else :
                ans[i+j+1] = c
    if (c != 0):
        if (l == i+j+1):
            ans += [c]
            l += 1
        else:
            ans[i+j+1] = c

    result = ""
    if (flag):
        result += '-'
    for i in range(0,l)[::-1]:
        result += str(ans[i])

    return result

print multiply("1234","-3933")
print multiply("0","-3933")
print multiply("-9999","-9999")
