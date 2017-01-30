def dic(ch):
    if(ch=='0'):
        return [' ']
    elif (ch=='1'):
        return ['1']
    elif (ch=='2'):
        return ['a','b','c']
    elif (ch=='3'):
        return ['d','e','f']
    elif (ch=='4'):
        return ['g','h','i']
    elif (ch=='5'):
        return ['j','k','l']
    elif (ch=='6'):
        return ['m','n','o']
    elif (ch=='7'):
        return ['p','q','r','s']
    elif (ch=='8'):
        return ['t','u','v']
    elif (ch=='9'):
        return ['w','x','y','z']
    else:
        return [ch]

def letterCombinations(digits):
    ans=[[],[]]
    tag=1
    for le in digits:
        tag = not tag
        letters = dic(le)
        ans[tag] = []
        for ch in letters:
            l = len(ans[not tag])
            if (l == 0):
                a = ""+ch
                ans[tag] += a
            else:
                for i in range(0,l):
                    a = ans[not tag][i]+ch
                    ans[tag]+='a'
                    ll = len(ans[tag])
                    ans[tag][ll-1] = a
    return ans[tag]
    

print(letterCombinations('2034'))
