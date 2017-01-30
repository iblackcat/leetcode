def comb(c, target, start):
    ans = []
    l = len(c)
    if (start >= l):
        return []
    i = start
    while (i < l):
        if (c[i] > target):
            break
        elif (c[i] == target):
            ans += [[c[i]]]
        else :
            tmp = comb(c, target-c[i], i+1)
            for j in tmp:
                ans += [[c[i]]+j]
        i += 1
        while (i < l and c[i] == c[i-1]):
            i += 1
    return ans

def combinationSum2(candidates, target):
    candidates = sorted(candidates)
    return comb(candidates, target, 0)

print combinationSum2([10,1,2,7,6,1,5,0], 8)
print combinationSum2([10,1,2,7,6,1,5,0], 0)
