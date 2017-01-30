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

def threeSum(nums):
    ans = []
    l = len(nums)
    if (l < 3):
        return ans
    nums = q_sort(nums)
    for i in range(0,l-2):
        if (i != 0 and nums[i] == nums[i-1]):
            continue
        for j in range(i+1,l-1):
            if (j != i+1 and nums[j] == nums[j-1]):
                continue
            su = nums[i]+nums[j]
            if (find(-su, nums[j+1:])):
                ans += [[nums[i],nums[j],-su]]
    return ans

nu = [3,0,-2,-1,1,2]
print(threeSum(nu))
