def find_mi(nums,target,s,t):
    if (s >= t):
        return -1
    mid = ((s+t)>>1)
    if (nums[mid] == target and (mid == 0 or nums[mid-1]<target)):
        return mid
    elif (nums[mid] >= target):
        return find_mi(nums,target,s,mid)
    else:
        return find_mi(nums,target,mid+1,t)

def find_ma(nums,target,s,t):
    l = len(nums)
    if (s >= t):
        return -1
    mid = ((s+t)>>1)
    if (nums[mid] == target and (mid == l-1 or nums[mid+1]>target)):
        return mid
    elif (nums[mid] <= target):
        return find_ma(nums,target,mid+1,t)
    else:
        return find_ma(nums,target,s,mid)

def searchRange(nums, target):
    l = len(nums)
    s = find_mi(nums,target,0,l)
    if (s == -1):
        return [-1,-1]
    t = find_ma(nums,target,0,l)
    return [s,t]

a = [5,7,7,8,8,10]
print(searchRange([], 6))
