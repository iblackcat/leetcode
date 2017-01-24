import time

def check(s, start, end, f, max):
    l = len(s)
    f[start][end] = 1
    if (max < end - start + 1):
        max = end - start + 1
    if (start > 1 and s[start-2] == '(' and s[start-1] == ')' and f[start-2][end] == 0):
        max = check(s, start-2, end, f, max)
    if (end < l-2 and s[end+1] == '(' and s[end+2] == ')' and f[start][end+2] == 0):
        max = check(s, start, end +2, f, max)
    if (start > 0 and end < l-1 and s[start-1]=='(' and s[end+1]==')' and f[start-1][end+1]==0):
        max = check(s, start-1, end+1, f, max)
    return max

def longestValidParentheses(s):
    max = 0
    l = len(s)
    count = 0
    stack = 0
    last = 0
    for i in range(0, l):
        if (s[i] == '('):
            if (count == 0):
                last = i
            stack += 1
            count += 1
        else :
            if (stack == 0):
                if (count > max):
                    max = count
                count = 0
            else :
                count += 1
                stack -= 1
    if (stack > 0):
        stack = 0
        count = 0
        i = l-1
        while (i >= last):
            if (s[i] == ')'):
                stack += 1
                count += 1
            else :
                if (stack == 0):
                    if (count > max):
                        max = count
                    count = 0
                else :
                    count += 1
                    stack -= 1
            i -= 1
        if (count > max):
            max = count
    elif (count > max):
        max = count
    return max

print time.time()
print time.localtime(time.time())
print longestValidParentheses("))))())(())()))(()()(())(())()))(((()()))()()))(())(())()())()(()())((()(((())()())(()())(())((()))))())()))()(())))())()))(()))((()())((()(())))(()))))))))((())(()()((())()()(()))))(((()(())))())))()())))())()()())()(())()(((())()))()()())))()())))()((((((())((())))((())())(((()())())()((((((()())((()()(())(()))(()())()))()(()(()())(()))((())((())))))()()))))()())()))))((((())(())))((()))(()()()()()((())((((())())()())()())(()(()()))())(((()())(()))()))(())()((()(())))))()())())()()(())))((())()()()))(())((()())))))((()((((()(((())()))))(()))()()))(()(())(()((()()()))))()))()()(((()()(())())()(())(()()()))()(()())))()((()((()))))())()(())()(()()((()()())(((())((())))(()())))()))()()())()))((()))(((()()()((()))))()()()))()))())())))))())()))(()))))(()()()))()((())))((())))()))(()()()()()()(()))())())(((())))(())(()(()())((()()()()))()()(()()))(()())(()()()((()()(((()(()((()((((()((())((()()))))))()())())(()(())()((((()()()()()))))()())()((())))))))()(((()())))()(()()(()()()()))()((((()((())(())))())))(()()()())()))))))((()))())((())(()(()(((()()()((((()()))())()())()())()))))())()(((()))))()()())))(())())))(())())((()))(())))(((()()))((((()))(()()))())((()())(()))(()(())(()(()))((((((()()(()()(()))()(()(())((((((((()(()())((())))())()())(()(()()))))(()(()()()))(()((()(((())((())(())()(()()())(()))())((()((((((())())(())()(()()(()())(())())()()))())(()))(())))()())))()()((()))())()()(())(()())()())())())))()()))((((()((()(())(((())()((())(())())))))()(()))())()))())(((())))))((((()(()()))))(((())(((())((())))))()()))()(()(((((((()))))((()))())()(())()))())())((()))))((())(())))(((())((((()(())(())()(((((())))()))()(()())(()()(())()(((()))())())))()))()()())((")
print time.time()
print time.localtime(time.time())
print longestValidParentheses('()()')
print longestValidParentheses('())()()))')
print longestValidParentheses(')()())')
print longestValidParentheses(")()(((())))(")
print longestValidParentheses('()((())')
print longestValidParentheses('()))((())')