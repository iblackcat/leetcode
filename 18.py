q_sort= lambda l: l if len(l)<=1 else q_sort([x for x in l[1:] if x<l[0]])+[l[0]]+q_sort([x for x in l[1:] if x>=l[0]])        

def find(num, nums):
    l = len(nums)
    if (l < 1):
        return 0
    mid = nums[int((l-1)/2)]
    if (mid == num):
        return 1
    elif (num < mid):
        return find(num, nums[:int((l-1)/2)])
    else :
        return find(num, nums[int((l-1)/2)+1:])

def threeSum(nums, target):
    ans = []
    l = len(nums)
    nums = q_sort(nums)
    for i in range(0,l-3):
        if (i != 0 and nums[i] == nums[i-1]):
            continue
        for j in range(i+1,l-2):
            if (j != i+1 and nums[j] == nums[j-1]):
                continue
            su = target-nums[i]-nums[j]
            if (su<(nums[j+1]<<1) or su>(nums[l-1]<<1)):
                continue
            for k in range(j+1, l-1):
                if (k != j+1 and nums[k] == nums[k-1]):
                    continue
                su = target-nums[i]-nums[j]-nums[k]
                if (su<nums[k+1] or su>nums[l-1]):
                    continue
                if (find(su, nums[k+1:])):
                    ans += [[nums[i],nums[j],nums[k],su]]
    return ans

nu = [3,2,4,5,0,-1,-2]
print(threeSum(nu, 6))
