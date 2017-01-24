def find(f,ans,s,t,st,mo):
    print(f,ans,s,t,st,mo)
    m=(s+t)/2
    if f[m]==st:
        ans[m]+=[mo]
        return -1
    elif f[m]<st:
        if m==t:
            return m+1
        else:
            return find(f,ans,m+1,t,st,mo)
    else :
        if m==s:
            return m
        else:
            return find(f,ans,s,m-1,st,mo)

def groupAnagrams(strs):
    le=len(strs)
    if le==0:
        return []
    ans=[[strs[0]]]
    model=[''.join(sorted(strs[0]))]
    i=1
    for j in range(1,le):
        tmp=''.join(sorted(strs[j]))
        loc=find(model,ans,0,i-1,tmp,strs[j])
        print(loc)
        if loc<0:
            continue
        elif loc>=i:
            ans+=[[strs[j]]]
            model+=[tmp]
            i+=1
        else:
            ans+=[[]]
            model+=[[]]
            for k in range(i,loc,-1):
                ans[k]=ans[k-1]
                model[k]=model[k-1]
            ans[loc]=[strs[j]]
            model[loc]=tmp
            i+=1
    return ans

print(groupAnagrams(["ape","and","cat"]))
