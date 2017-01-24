def maxSubArray(nums):
    size=len(nums)
    f=[[0]*size]*size
    for i in range(0,size):
        f[i][i]=nums[i]
    for i in range(1,size+1):
        for j in range(0,)
