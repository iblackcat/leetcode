def maxArea(height):
    l = len(height)
    if (l < 2):
        return 0
    ans = min(height[0], height[l-1])*(l-1)
    maxNum = max(height)
    i = l-1
    j = 0
    while (i>1):
        if (maxNum*(i-1) < ans):
            return ans
        if (height[j] < height[j+i]):
            j += 1
        if (min(height[j],height[j+i-1])*(i-1) > ans):
            ans = min(height[j],height[j+i-1])*(i-1)
        i -= 1
    return ans

def mmm(height):
    a=0
    b=0
    
    l = len(height)
    if (l < 2):
        return 0
    ans = 0
    for i in range(0, l-1):
        for j in range(i+1, l):
            if (min(height[i],height[j])*(j-i) > ans):
                ans = min(height[i],height[j])*(j-i)
                a = i
                b = j
    print(a,b)
    return ans

h = [2,0,0,1,1,2,3,4,5,0,0,0,1,100,2,1,6,7,8,9,10,0,0,0,2,3,4,5,6,5,4,3,2,1]
print(maxArea(h))
print(mmm(h))
