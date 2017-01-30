q_sort= lambda l: l if len(l)<=1 else q_sort([x for x in l[1:] if x<l[0]])+[l[0]]+q_sort([x for x in l[1:] if x>=l[0]])        

def s_find(target, nums, s, t):
    if (target < nums[s]):
        return nums[s]
    elif (target > nums[t]):
        return nums[t]
    mid = int((s+t)/2)
    if (nums[mid] == target):
        return nums[mid]
    elif (target < nums[mid]):
        if (target > nums[mid-1]):
            return nums[mid] if abs(target-nums[mid-1])>abs(target-nums[mid]) else nums[mid-1]
        return s_find(target, nums, s, mid-1)
    else :
        if (target < nums[mid+1]):
            return nums[mid+1] if abs(target-nums[mid])>abs(target-nums[mid+1]) else nums[mid]
        return s_find(target, nums, mid+1, t)

def threeSum(nums, target):
    tag = 0
    ans = 0
    l = len(nums)
    nums = q_sort(nums)
    for i in range(0,l-2):
        if (i != 0 and nums[i] == nums[i-1]):
            continue
        for j in range(i+1,l-1):
            if (j != i+1 and nums[j] == nums[j-1]):
                continue
            su = nums[i]+nums[j]
            su += s_find(target-su, nums, j+1, len(nums)-1)
            if (tag == 0 or abs(su-target) < abs(ans-target)):
                ans = su
                tag = 1
    return ans

nu = [3,0,-2,-1,1,2]
print(threeSum(nu, 7))
