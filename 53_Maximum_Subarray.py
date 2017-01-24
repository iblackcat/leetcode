def maxSubArray(nums):
    ans=0
    new_nums=[]
    n=len(nums)
    if (n==0):
        return 0
    ans=nums[0]
    tmp=nums[0]
    for i in range(1,n):
        if (nums[i]>ans): ans=nums[i]
        if (tmp*nums[i]>=0):
            tmp+=nums[i]
        else:
            new_nums+=[tmp]
            tmp=nums[i]
    new_nums+=[tmp]
    n=len(new_nums)
    tag=[0]*n
    index=0
    if (new_nums[0]<=0): index=1
    if (n<=index): return ans
    tmp=new_nums[index]
    ans=tmp
    while (index+2<n):
        tmp+=new_nums[index+1]+new_nums[index+2]
        if (new_nums[index+2]>tmp):
            tmp=new_nums[index+2]
        if (tmp>ans):
            ans=tmp
        index+=2
    return ans

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

