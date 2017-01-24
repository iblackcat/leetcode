def permuteUnique(nums):
    nums=sorted(nums)
    size=len(nums)
    lim=[]
    now=[]
    j=0
    for i in range(0,size):
        if i!=0 and nums[i]==nums[i-1]:
            lim[j-1]+=1
        else:
            lim+=[1]
            nums[j]=nums[i]
            now+=[nums[i]]
            j+=1
    nsize=j
    loc=[-1]*size
    tag=[0]*nsize
    ans=[]
    j=0
    while j>=0:
        if loc[j]>=0:
            tag[loc[j]]-=1
        loc[j]+=1
        while loc[j]<nsize and tag[loc[j]]>=lim[loc[j]]:
            loc[j]+=1
        if loc[j]>=nsize:
            loc[j]=-1
            j-=1
            continue
        else:
            tag[loc[j]]+=1
            j+=1
        if j>=size:
            tmp=[]
            for i in range(0,size):
                tmp+=[nums[loc[i]]]
            ans+=[tmp]
            j-=1
    return ans
print(permuteUnique([1,0,1,2]))
        
