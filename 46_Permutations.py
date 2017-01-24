def permute(nums):
    size=len(nums)
    now=[0]*size
    loc=[0]*size
    tag=[1]*size
    for i in range(0,size):
        now[i]=nums[i]
        loc[i]=i
    j=size-1
    ans=[]
    tmp=[0]*size
    for i in range(0,size):
        tmp[i]=now[i]
    ans+=[tmp]
    while(j>=0):
        if loc[j]>=0:
            tag[loc[j]]=0
        loc[j]+=1
        while loc[j]<size and tag[loc[j]]!=0:
            loc[j]+=1
        if loc[j]>=size:
            loc[j]=-1
            now[j]=-1
            j-=1
            continue
        else:
            tag[loc[j]]=1
            now[j]=nums[loc[j]]
            j+=1
        if j>=size:
            tmp=[0]*size
            for i in range(0,size):
                tmp[i]=now[i]
            ans+=[tmp]
            j-=1
    return ans
print(permute([1,2,3]))
