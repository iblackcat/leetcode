def find(f, s, t, target):
    mid = (s+t)>>1
    if (target >= f[mid] and (mid == 0 or target < f[mid-1])):
        return mid
    elif (target >= f[mid]):
        return find(f, s, mid-1, target)
    elif (target < f[mid] and mid == t):
        return -1
    else:
        return find(f, mid+1, t, target)

def jump(nums):
    l = len(nums)
    if (l <= 1):
        return 0
    ans = [l-1]
    la = 1
    for i in range(0,l-2)[::-1]:
        if (nums[i] == 0):
            continue
        else :
            tmp = find(ans, 0, la-1, nums[i]+i)
            print tmp,ans,0,la-1,nums[i]+i
            if (tmp == -1):
                continue
            elif (tmp +1 == la):
                ans += [i]
            else :
                ans[tmp+1] = [i]
                la = tmp+1
    return tmp

print jump([2,3,1,1,4])
