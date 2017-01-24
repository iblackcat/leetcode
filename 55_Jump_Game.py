def canJump(nums):
    n=len(nums)
    last=0
    now=0
    while now<=last and last<n-1:
        if now+nums[now]>last:
            last=now+nums[now]
        now+=1
    return last>=n-1

print(canJump([3,2,1,0,4]))
