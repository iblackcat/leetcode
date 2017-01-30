def add(height, s, t, ma):
    ans = 0
    for i in range(s, t):
        if (ma - height[i] > 0):
            ans += ma - height[i]
    return ans

def trapFromLeft(height, loc):
    ans = 0
    tmp = 0
    pos = -1
    for i in range(0, loc):
        if (height[i] > tmp):
            if (pos != -1):
                ans += add(height, pos, i, tmp)
            tmp = height[i]
            pos = i
    if (pos != -1):
        ans += add(height, pos, loc, tmp)
    return ans
        
def trapFromRight(height, loc):
    l = len(height)
    ans = 0
    tmp = 0
    pos = -1
    i = l-1
    while (i > loc):
        if (height[i] > tmp):
            if (pos != -1):
                ans += add(height, i, pos, tmp)
            tmp = height[i]
            pos = i
        i -= 1
    if (pos != -1):
        ans += add(height, loc, pos, tmp)
    return ans

def trap(height):
    l = len(height)
    ma = 0
    pos = -1
    for i in range(0,l):
        if (height[i] > ma):
            ma = height[i]
            pos = i
    if (pos == -1):
        return 0
    return trapFromLeft(height, pos) + trapFromRight(height, pos)

print trap([0,1,2,2,1,1,1,4,1,1,1,1])
    
