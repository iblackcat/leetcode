def solveNQueens(n):
    result=[]
    ans=[-1]*n
    raw=[0]*n
    lflag=[0]*(n+n-1)
    rflag=[0]*(n+n-1)
    i=0
    while i>=0:
        if ans[i]>=0:
            raw[ans[i]]=0
            lflag[i+ans[i]]=0
            rflag[i-ans[i]+n-1]=0
        ans[i]+=1
        while ans[i]<n and (raw[ans[i]]==1 or lflag[i+ans[i]]==1 or rflag[i-ans[i]+n-1]==1):
            ans[i]+=1
        if ans[i]>=n:
            ans[i]=-1
            i-=1
            continue
        else :
            raw[ans[i]]=1
            lflag[i+ans[i]]=1
            rflag[i-ans[i]+n-1]=1
            i+=1
        if i>=n:
            tmp=[]
            for j in range(0,n):
                tmp+=[ans[j]]
            result+=[tmp]
            i-=1
    ans=[]
    for i in range(0,len(result)):
        ttt=[]
        for j in range(0,n):
            tmp=""
            for k in range(0,n):
                if result[i][j]!=k:
                    tmp+='.'
                else :
                    tmp+='Q'
            ttt+=[tmp]
        ans+=[ttt]
    return len(ans)
print(solveNQueens(6))
