def comb(c, target, start):
    l = len(c)
    ans = []
    for i in range(start, l):
        if (c[i] > target):
            break
        elif (c[i] == target):
            ans += [[c[i]]]
        else:
            temp = comb(c, target-c[i], i)
            for j in temp:
                ans += [[c[i]]+j]
    return ans

def combinationSum(candidates, target):
    candidates = sorted(candidates)
    return comb(candidates, target, 0)

print combinationSum([8,7,4,3], 11)
